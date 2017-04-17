Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Screen()
<turtle._Screen object at 0x0375F550>
>>> wn=turtle.Screen()
>>> t1=turtle.Turtle()
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> wn]
SyntaxError: invalid syntax
>>> wn
<turtle._Screen object at 0x0375F550>
>>> print type(wn)
SyntaxError: invalid syntax
>>> print type(wn)
SyntaxError: invalid syntax
>>> type(t1)
<class 'turtle.Turtle'>
>>> wn.setup(500.500)
>>> wn.setup(500.500)
>>> wn.setup(500.100)
>>> wn.setup(100.500)
>>> wn.setup(500.500)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.colormode(255)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t1.colormode(255)
AttributeError: 'Turtle' object has no attribute 'colormode'
>>> wn.colormode(255)
>>> t1.fd(100)
>>> t1.pencolor('red')
>>> t1.forward(50)
>>> t1.pencolor((0.100.200))
SyntaxError: invalid syntax
>>> wn.colormode(255)
>>> t1.pencolor((0.100.200))
SyntaxError: invalid syntax
>>> t1.pencolor((0,100,200))
>>> t1.shape('turtle')
>>> wn.addshape('C:\Users\400T6B\Downloads\rocketship.gif')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> C:\Users\400T6B\Downloads\rocketship.gif
SyntaxError: unexpected character after line continuation character
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> t1.shape('rocketship.gif')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t1.shape('rocketship.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named rocketship.gif
>>> t1.shape("rocketship.gif")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t1.shape("rocketship.gif")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named rocketship.gif
>>> t1.shape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> t1.fd(50)
>>> 
