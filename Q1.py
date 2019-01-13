s='{name} has {n} messages'
s=s.format(name='Nikesh',n=37)
print(s)

import textwrap
s="Labore voluptate ullamco anim fugiat reprehenderit voluptate duis consectetur. Exercitation fugiat adipisicing qui consequat aliqua voluptate. Nostrud commodo est excepteur nostrud et pariatur do eiusmod. Occaecat mollit proident enim magna irure deserunt laborum. Aliquip culpa in laboris tempor nostrud duis pariatur ut Lorem consequat quis excepteur dolore reprehenderit. Enim sint nulla mollit deserunt ipsum est Lorem non cupidatat esse. Excepteur in sunt nisi deserunt non do adipisicing ipsum. Qui ex magna laborum est."
print(textwrap.fill(s,10))    #Wraps the text 
print(textwrap.fill(s,100,initial_indent='  - '))
print(textwrap.fill(s,100,subsequent_indent='  - '))