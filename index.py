#Program-01
import textwrap
s = '{name} has {n} messages'
s = s.format(name='Nikesh', n=37)
print(s)

#Program-02
s = 'Hello'
print(textwrap.fill(s, 1))  # Wraps the text
print(textwrap.fill(s, 1, initial_indent='  - '))
print(textwrap.fill(s, 1, subsequent_indent='  - '))

#Program-03
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s,quote=False)) #Disabling escape of quotes
round(1.27,1)
round(-1.27,1)
round(1.2568,3)
a=12456
round(a,-3)

#Program-04
x=1.23456789
format(x,'0.3f')
'value is {:0.3f}'.format(x)

a=2.155
b=4.211
c=a+b
c=round(c,2)
print(c)
c=format(c,'0.2f')
print(c)

#Program-05
x=12345
bin(x)  #Converts to binary - Prints  '0b11000000111001'
oct(x)  #Converts to Octal  - Prints  '0o30071'
hex(x)  #Converts to Hexadecimal  - Prints  '0x3039'

#Now to remove oo, ob and ox

format(x,'b') #Prints 11000000111001
format(x,'o') #Prints 30071
format(x,'x') #Prints 3039