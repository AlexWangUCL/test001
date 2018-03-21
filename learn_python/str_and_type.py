# -*- coding: utf-8 -*-

s1 = 72
s2 = 85

improve = s2 - s1
r = improve/s1*100
print('Hello, {0} grades improved {1:.1f}%'.format('小明', r))
#print('恭喜{0}童鞋，你比去年多考了{1}分，提升了{2:.1f}%'.format(name,dif,r))
print('小明今年的成绩与去年相比提升了 %2.1f%%' % r)