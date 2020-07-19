#!/usr/bin/env python3

#Convert Cycling miles to steps

num1 = float(input('Enter cycling miles: '))
num2 = int(5280) # 1 mile = 5280 feet
num3 = float(2.5) # my stride length in feet

#num3 = float(input('Enter your stride in feet: '))

total = (num1 * num2) / num3 # gives total steps


print('Total distance of',num1 ,'cycling miles to steps is:',total)
