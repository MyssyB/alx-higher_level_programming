#!/usr/bin/python3

# Add your doctests here:
"""
>>> a_list[3]
42
>>> a_list[6]
'Ni!'
>>> len(a_list)
8

>>> b_list[1:]
['Stills', 'Nash']
>>> group = b_list + c_list
>>> group[-1]
'Young'

>>> 'war' in mystery_list
False
>>> 'peace' in mystery_list
True
>>> 'justice' in mystery_list
True
>>> 'oppression' in mystery_list
False
>>> 'equality' in mystery_list
True

>>> range(a, b, c)
[5, 9, 13, 17]
"""

# Write your python code here:

a_list = [1, 2, 3, 42, 'a', 'b', 'Ni!', 'Beulah']
b_list = ['unknown', 'Stills', 'Nash']
print(b_list[1:])
c_list = ['Young']
group = b_list + c_list

mystery_list = ['fight', 'justice', 'peace', 'equality']






if __name__ == '__main__':
    import doctest
    doctest.testmod()
