
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

x = int(((2*glass_size)-(straw_pos)))
#after that, because x may be odd number, I took the integer form of result of the division x by 2  and I add 2 (because of the equation that I create) to find the drinkable line
for n in range(int(x/2)+2):
    # Secondly, I made a loop to write pipe.
    for b in range(straw_pos):
        print('',end='')
        for x in range(b):
            print(' ',end='')
        print('o')
    # the line that we will drink depends on the n number , so I wrote a equation and loop to drink line(s) that we can drink
    for i in range(n):
        for l in range(i):
            print(' ',end='')
        print('\\',end='')
        for m in range(straw_pos-1):
            print(' ',end='')
        print('o',end='')
        for c in range(x- 2*i):
            print(' ',end='')
        print('/')
    # After we drink the line, we have to continue our lines which consist of '*' , to calculate these lines I made an equation and I create loop which depends on 'n'
    for a in range(glass_size-n):
        for t in range(a+n):
            print(' ',end='')
        print('\\',end='')
        for p in range((2*(glass_size) -2* (a+n))):
            print('*',end='')
        print('/')
    # Also, a line to write the bottom of the glass.
    print(' '*(glass_size)+'--')
    # I wrote space times glass_size and I add '||' to write the stalk
    for i in range(glass_size):
        print(' '*(glass_size)+'||')


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


