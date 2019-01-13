import textwrap
s = '{name} has {n} messages'
s = s.format(name='Nikesh', n=37)
print(s)

s = 'Hello'
print(textwrap.fill(s, 1))  # Wraps the text
print(textwrap.fill(s, 1, initial_indent='  - '))
print(textwrap.fill(s, 1, subsequent_indent='  - '))

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

x=1.23456789
format(x,'0.3f')
'value is {:0.3f}'.format(x)

a=2.1
b=4.2
c=a+b
c=round(c,2)
print(c)
c=format(c,'0.2f')
print(c)