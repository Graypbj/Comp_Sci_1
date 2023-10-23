import sys
from time import sleep
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)

par = int(input('\nWhat is par for this hole: '))
score = int(input('What did you shoot on this hole: '))

if (score - par) == 0:
    print('You shot par on this hole. Not bad')
elif (score - par) == -1:
    print('You shot a birdy on that hole. Let\'s hope it\'s able to continue living')
elif (score - par) == -2:
    print('You shot an eagle on that hole. The police want to know your location')
elif (score - par) == -3:
    print('You had an Albatross on that hole. That\'s a big ol bird')
elif(score - par) == 1:
    print('You bogeyed the hole you discombobulated ninny')
elif(score - par) > 1:
    print('You\'re not very good at golf')
