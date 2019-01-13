# iaeste-python

## Intro to Jupyter

1. Goto Anaconda Prompt
2. Enter 'jupyter notebook'
3. It opens Jupyter Notebook which  uses localhost

### What is Jupter Notebook

Jupyter is similar IDE like VSCode 

## Intro to Python

### Substitution of variables in Strings

Since Python doesn't have substitution of variables, we need to use a function called format() to redefine variables in a string

eg.
```python
s='{name} has {n} messages'
s=s.format(name='Nikesh',n=37)
print(s)
```

### Text-wrapping and indentation

By importing textwrap we can limit area spanned by a string in the console and we can provide initial indentation as well as subsequent indentation

eg.
```python
s='Hello World'
print(textwrap.fill(s,1))    #Wraps the text 
print(textwrap.fill(s,1,initial_indent='  - '))   #Adds ' - ' at the start of each line
print(textwrap.fill(s,1,subsequent_indent='  - '))    #Adds ' - ' after every line except the first one
```

### Replacing HTML/XML entities such as &entity; / &#code; with corresponding text Alternatively, you need to produce the text but escape certain characters (<,>,& etc)

So this basically converts the text to its HTML form

```python
s = 'Elements are written as "<tag>text</tag>".'  #allocation starts from right to left
import html
print(s)
print(html.escape(s))
print(html.escape(s,quote=False)) #Disabling escape of quotes
```

### Rounding off

This is done with the help of round(x,y) where x is the integer/float and y is the decimal points to be rounded off to given power of 10

```python
round(1.27,1)
round(-1.27,1)
round(1.2563,3)
a=12456
round(a,-3) #prints 12000 which is rounding  off to 10e3
```

Many time format is used for precision formatting

```python
x=1.23456789
format(x,'0.3f')
'value is {:0.3f}'.format(x)
```

### Converting integers to binary, octal, hexadecimal

The program  below converts to decimal, binary and so on

```python
x=12345
bin(x)  #Converts to binary - Prints  '0b11000000111001'
oct(x)  #Converts to Octal  - Prints  '0o30071'
hex(x)  #Converts to Hexadecimal  - Prints  '0x3039'
```
The program below does the same as above but removes the initial
```python
format(x,'b') #Prints 11000000111001
format(x,'o') #Prints 30071
format(x,'x') #Prints 3039
```

### Working with Linux

- Level of work

----------
| XYZ |
----------
| Horton |
----------
| VMWare |
----------
| Windows OS |
----------