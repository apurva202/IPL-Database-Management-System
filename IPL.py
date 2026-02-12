import AdminLogin
import UserLogin
import os
import time
import sys

def IPL():
    while True:    
        os.system('cls')

        print('#'*20,"WELCOME INDIAN PREMIER LEAGUE",'#'*20)
        print(' '*15,'SELECT THE INTERFACE IN WHICH YOU WANT TO WORK')
        print('1. Admin Interface')
        print('2. User Interface')
        print('3. Exit')

        ch=int(input('Enter your choice : '))
        if ch == 1:
            AdminLogin.AdminLogin()
        elif ch == 2:
            UserLogin.UserLogin()
        elif ch == 3:
            sys.exit()
        else:
            os.system('cls')
            print('Invalid option')
            time.sleep(1.3)

if __name__ == '__main__':
    IPL()