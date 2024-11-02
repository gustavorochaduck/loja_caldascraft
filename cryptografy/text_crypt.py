import time
import functions as fc

print('''if you are using the program for the first time, I recommend that you select [Library installation]. 
If you have the bcrypt library in version 4.2.0, you can start the program [RUN].''')

print('-=-'*20)
print('1 - [RUN]')
print('2 - [installation]')
print('-=-'*20)
selection = int(input('Select: '))
print('-=-'*20)

if selection == 1:
    print('1 - [view hashed list]')
    print('2 - [hashing a text]')
    print('-=-'*20)
    selection1 = int(input('Select: '))

    if selection1 == 1:
        fc.view_list

    elif selection1 == 2:
        text = input('Type the Text: ')
        hash_var = fc.hashed(text)
        print(fc.hashed(text))
        print('-=-'*20)
        print('You want to Save?')
        add_confirm = str(input('Type [Y] to yes and [N] to no: ').lower())
        
        if add_confirm == 'y':
            fc.add_desafio(fc.hashed(text))
        
        if add_confirm == n:
            input('Type [ENTER] to close the program: ')

elif selection == 2:
    fc.installation()