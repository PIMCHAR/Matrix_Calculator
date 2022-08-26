import numpy as np
import PySimpleGUI as sg
import os

sg.theme('darkgreen6')
method_matrix = ['sum', 'minus', 'mutiply matrix', 'multiply num', 'det', 'minor', 'cofactor']
keys_to_clear = ['num', 'a', 'b']
f = open('history.txt','w')
line = 0
check =['1','2','3','4','5','6','7','8','9','0',' ','\n']

def history(result):
    global line
    line+=1
    f = open('history.txt','a')
    f = f.write(str(values['met'])+'['+'a ='+
                str(values['a'].replace('\n','/'))+']'+'['+'b ='+
                str(values['b'].replace('\n','/'))+']'+'ans ='+
                (str(result).replace('\n','/'))+'\n')

def sum(matrix_A, matrix_B):
    return matrix_A + matrix_B

def minus(matrix_A, matrix_B):
    return matrix_A - matrix_B


def multiply_metrix(matrix_A, matrix_B):
    mul = []
    mult_A = np.array(matrix_A)
    mult_B = np.array(matrix_B)
    matrix_Bt = np.transpose(mult_B)
    shapeA = np.shape(mult_A)
    shapeB = np.shape(mult_B)
    for n1 in range(shapeA[0]):
        for n2 in range(shapeB[1]):
            row_col = np.sum(mult_A[n1] * matrix_Bt[n2])
            mul.append(row_col)
    return np.matrix(mul).reshape(shapeA[0], shapeB[1])

def multiply_num(num, matrix_A):
    return num * matrix_A

def det(matrix_A):
    return int(np.linalg.det(matrix_A))

def minor(num, matrix_A):
    num = num.split(',')
    rowA = int(num[0])
    colA = int(num[1])
    minorA = np.transpose(np.delete(np.transpose(np.delete(matrix_A, rowA - 1, 0)), colA - 1, 0))
    return det(minorA)

def cofactor(num, matrix_A):
    num = num.split(',')
    rowA = int(num[0])
    colA = int(num[1])
    minorA = np.transpose(np.delete(np.transpose(np.delete(matrix_A, rowA - 1, 0)), colA - 1, 0))
    return ((-1) ** (rowA + colA)) * det(minorA)

def call_mat(key):
    mat_k = []
    nub = 0
    col = 0
    row = values[key].split(sep='\n')
    for i in row:
        col = i.split()
    for i in values[key].split():
        mat_k.append(int(i))
    mat_k = np.matrix(mat_k)
    return (mat_k.reshape(len(row), len(col)))

def place(ele):
    return sg.Column([[ele]], pad=(0, 0), justification='r')

def reset():
    for key in keys_to_clear:
        window[key]('')
    window['answer'].update('')

def b_call():
    window['answer'].update(result)

input_matrix = [
    [
        place(sg.Text('number', key='namenum', pad=(15, 0))),
        place(sg.Text('matrix A', key='namea', pad=(20, 0))),
        place(sg.Text('matrix B', key='nameb', pad=(24, 0)))
    ],
    [
        place(sg.In(size=(8, 1), key='num', pad=(10, 0))),
        place(sg.Multiline(size=(8, 4), key='a')),
        place(sg.Text('+', key='sign')),
        place(sg.Multiline(size=(8, 4), key='b'))
    ]]

txt_ans = [[sg.Text('ANSWER =', pad=(0, 10)), sg.Text('', key='answer')]]

layout = [
    [sg.Text('Matrix Calculator', font=(None, 14)),
     sg.Text(':\tPlease enter only complex numbers', font=(None, 10))],
    [sg.Text('select your method')],
    [
        sg.Listbox(list(method_matrix), size=(14, 7), key='met', enable_events=True),
        sg.Frame('Input', input_matrix, key=('inp'), visible=False)
    ],
    [
        sg.Button('back', size=(4, 0)),
        sg.Button('clear', size=(4, 0), pad=(30, 0)),
        sg.Button('cal', size=(5, 1), pad=(0, 0))
    ],
    [sg.Column(txt_ans, justification='c')],
]

window = sg.Window(' Matrix Calculator ', layout, size=(480, 300))


def mat_mat():
    window['inp'].update(visible=True)
    window['namenum'].update(visible=False)
    window['namea'].update(visible=True)
    window['nameb'].update(visible=True)
    window['num'].update(visible=False)
    window['a'].update(visible=True)
    window['sign'].update(visible=True)
    window['b'].update(visible=True)
    window['answer'].update('')


def num_mat():
    window['inp'].update(visible=True)
    window['namenum'].update('row,col', visible=True)
    window['namea'].update(visible=True)
    window['nameb'].update(visible=False)
    window['num'].update(visible=True)
    window['sign'].update(visible=False)
    window['b'].update(visible=False)
    window['answer'].update('')


def mat():
    window['inp'].update(visible=True),
    window['namenum'].update(visible=False)
    window['namea'].update(visible=True)
    window['nameb'].update(visible=False)
    window['num'].update(visible=False)
    window['sign'].update(visible=False)
    window['b'].update(visible=False)
    window['answer'].update('')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        f.close()
        break

    elif event == 'clear':
        reset()

    elif event == 'back' and line>1:
        f = open('history.txt','r')
        read_l = f.readlines()
        result=read_l[line-2]
        window['answer'].update('')
        b_call()

    elif values['met'] == ['sum']:
        mat_mat()
        window['sign'].update('+')
        if event == 'cal':
            if np.shape(call_mat('a')) == np.shape(call_mat('b')):
                result = sum(call_mat('a'), call_mat('b'))
                history(result)
                b_call()
            else:
                sg.popup('\t\t\t    ERROR!!!\n\nDIMENSION of matrixA must be equal to matrixB\n\nplease try again')
                reset()

    elif values['met'] == ['minus']:
        mat_mat()
        window['sign'].update('-')
        if event == 'cal':
            if np.shape(call_mat('a')) == np.shape(call_mat('b')):
                result = minus(call_mat('a'), call_mat('b'))
                history(result)
                b_call()
            else:
                sg.popup('\t\t\t    ERROR!!!\n\nDIMENSION of matrixA must be equal to matrixB\n\nplease try again')
                reset()

    elif values['met'] == ['mutiply matrix']:
        mat_mat()
        window['sign'].update('*')
        if event == 'cal':
            if np.shape(call_mat('a'))[1] == np.shape(call_mat('b'))[0]:
                result = (multiply_metrix(call_mat('a'), call_mat('b')))
                history(result)
                b_call()
            else:
                sg.popup('\t\t\t    ERROR!!!\n\nColumn of matrixA must be equal Row of matrixB\n\nplease try again')
                reset()

    elif values['met'] == ['multiply num']:
        num_mat()
        window['namenum'].update('number')
        if event == 'cal':
            result = multiply_num(int(values['num']), call_mat('a'))
            history(result)
            b_call()

    elif values['met'] == ['det']:
        mat()
        if event == 'cal':
            if np.shape(call_mat('a'))[0] == np.shape(call_mat('a'))[1]:
                result = det(call_mat('a'))
                history(result)
                b_call()
            else:
                sg.popup('\t    ERROR!!!\n\n Dimension must be square \n\nplease try again')
                reset()

    elif values['met'] == ['minor']:
        num_mat()
        if event == 'cal':
            if np.shape(call_mat('a'))[0] == np.shape(call_mat('a'))[1]:
                result = minor(values['num'], call_mat('a'))
                history(result)
                b_call()
            else:
                sg.popup('\t    ERROR!!!\n\n Dimension must be square \n\nplease try again')
                reset()

    elif values['met'] == ['cofactor']:
        num_mat()
        if event == 'cal':
            if np.shape(call_mat('a'))[0] == np.shape(call_mat('a'))[1]:
                result = cofactor(values['num'], call_mat('a'))
                history(result)
                b_call()
            else:
                sg.popup('\t    ERROR!!!\n\n Dimension must be square \n\nplease try again')
                reset()

    else:
        pass

os.remove("history.txt")
window.close()