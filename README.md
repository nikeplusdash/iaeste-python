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

### Replacing HTML/XML entities such as &entity; / &#code; with corresponding text

