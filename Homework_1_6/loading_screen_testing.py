import sys
from time import sleep

print('Booting up')
sleep(1)

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)

global attempt_index
attempt_index = 0


def last_directory():
    print('Last directory: C/user/jxt/5')


def run_jxt():
    global attempt_index
    # print('\nattempt_index inside the function is', attempt_index)
    password = input('Please input password: ')
    if password == 'Xj0t_51ha':
        print('Password correct')
        jxt_exe()
    else:
        print('Password incorrect, please try again')
        attempt_index += 1
        if attempt_index > 3:
            exit()
        run_jxt()


def jxt_exe():
    for j in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('=' * j, 1 * j))
        sys.stdout.flush()
        sleep(0.02)
    print('\nWelcome to jxt-5')


print('\nWelcome user. It\'s been a while')

print('(1) Open last directory\n'
      '(2) Run jxt-5\n'
      '(3) Exit program\n')

option_select = int(input('Enter selection from above: '))

if option_select == 1:
    last_directory()

if option_select == 2:
    run_jxt()

if option_select == 3:
    exit()

