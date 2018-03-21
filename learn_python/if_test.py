# -*- coding: utf-8 -*-

height = input('Please input your height: ')
weight = input('Please input your weight ')
h = float(height)
w = float(weight)
bmi = w/pow(h, 2)
if bmi < 18.5:
    print('too light')
elif bmi >= 18.5 and bmi < 25:
    print('good fit')
elif bmi >= 25 and bmi < 28:
    print('too weight')
elif bmi >= 28 and bmi < 32:
    print('fat')
else:
    print('fat heavily')