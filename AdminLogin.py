import os
import pwinput
from CREATE import CREATE
from MODIFY import MODIFY
from DELETE import DELETE
from ADD import ADD
import sys
import time
import IPL

def AdminLogin():
    os.system('cls')

    print('#'*75)
    print('#'*20,"WELCOME TO LOGIN SCREEN FOR ADMIN",'#'*20)
    print('#'*75)

    uname=input('Enter your user name : ')
    pwd=pwinput.pwinput()

    if uname=='patel' and pwd=='qwertyuiop':
        AdminInterface()
        
    else:
        os.system('cls')
        print('!!!Please check your user name and password!!!')
        time.sleep(2)
        AdminLogin()

def AdminInterface():
    os.system('cls')
    print(' '*15,'SELECT OPTION TO WORK')
    print('1. CREATE DATAFRAMES')
    print('2. ADD RECORDS IN DATAFRAMES')
    print('3. MODIFY RECORDS IN DATAFRAMES')
    print('4. DELETE RECORDS IN DATAFRAMES')
    print('5. Exit')
    print('6. Log Out')

    ch=int(input('Enter your choice :'))
    if ch == 1:
        CREATE()
    elif ch == 2:
        ADD()
    elif ch == 3:
        MODIFY()
    elif ch == 4:
        DELETE()
    elif ch==5:
        sys.exit()
    elif ch==6:
        IPL.IPL()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        AdminInterface()

if __name__ == "__main__":
    AdminLogin()