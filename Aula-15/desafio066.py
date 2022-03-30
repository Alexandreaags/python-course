from re import A
from xml.dom import InuseAttributeErr


while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    a = num * 1
    b = num * 2
    c = num * 3
    d = num * 4
    e = num * 5
    f = num * 6
    g = num * 7
    h = num * 8
    i = num * 9
    j = num * 10 

    if num > 0:
        print(f' {num} x 1 = {a}\n {num} x 2 = {b}\n {num} x 3 = {c}\n {num} x 4 = {d}\n {num} x 5 = {e}\n {num} x 6 = {f}\n {num} x 7 = {g}\n {num} x 8 = {h}\n {num} x 9 = {i}\n {num} x 10 = {j}')
    else:
        break