Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> complex(10,20)
(10+20j)
>>> a="CMRuniversity"
>>> a=[0:]
SyntaxError: invalid syntax
>>> a=[0: ]
SyntaxError: invalid syntax
>>> a=python
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=python
NameError: name 'python' is not defined
>>> type(a)
<class 'str'>
>>> a=("python")
>>> type(a)
<class 'str'>
>>> a[0:6]
'python'
>>> a[0:4]
'pyth'
>>> l=[10,20,30,[1,2,3],40]
>>> l[3][1]
2
>>> type(l)
<class 'list'>
>>> l(2)=300
SyntaxError: can't assign to function call
>>> t=910,20,30,40,50)
SyntaxError: invalid syntax
>>> t[1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[1]
NameError: name 't' is not defined
>>> l[6]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l[6]
IndexError: list index out of range
>>> a=("CMR")
>>> b=("university")
>>> c=print("a*b")
a*b
>>> c=("a*b")
>>> 
>>> 
>>> cmath.sqrt
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    cmath.sqrt
NameError: name 'cmath' is not defined
>>> cmath.sqrt(-1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    cmath.sqrt(-1)
NameError: name 'cmath' is not defined
>>> cmath.sqrt(-1)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    cmath.sqrt(-1)
NameError: name 'cmath' is not defined
>>> set1=[1,2,2,3,5,4}
SyntaxError: invalid syntax
>>> math.sqrt(49)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    math.sqrt(49)
NameError: name 'math' is not defined
>>> D={1:200,2:400,"pi":3.1416}
>>> D=["Pi"]
>>> D[2]=400
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    D[2]=400
IndexError: list assignment index out of range
>>> 
