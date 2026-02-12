import os
import pwinput
import Analysis
import sys
import time
import IPL

def UserLogin():
    os.system('cls')

    print('#'*74)
    print('#'*20,"WELCOME TO LOGIN SCREEN FOR USER",'#'*20)
    print('#'*74)

    uname=input('Enter your user name : ')
    pwd=pwinput.pwinput()

    if uname=='patel' and pwd=='qwertyuiop':
        UserInterface()        

    else:
        os.system('cls')
        print('!!!!Please check your user name and password!!!!')
        time.sleep(2)
        UserLogin()

def UserInterface():

    os.system('cls')

    print(' '*15,'SELECT OPTION TO WORK')
    print("1. Analyse Team's details")
    print("2. Analyse Most Runs details")
    print("3. Analyse Best Batting Strike Rate details")
    print("4. Analyse Most Hundreds details")
    print("5. Analyse Most Wickets details")
    print("6. Analyse Most 5 Wickets Haul details")
    print("7. Analyse Best Economy details")
    print('8. Exit')
    print('9. Log Out')
    
    ch=int(input('Enter your choice : '))
    if ch==1:
        Analysis.ATeam()
    elif ch==2:
        Analysis.AMostRuns()
    elif ch==3:
        Analysis.ABestStrikeRate()
    elif ch==4:
        Analysis.AMostHundreds()
    elif ch==5:
        Analysis.AMostHundreds()
    elif ch==6:
        Analysis.A5WicketHaul()
    elif ch==7:
        Analysis.ABestEconomy()
    elif ch==8:
        sys.exit()
    elif ch==9:
        IPL.IPL()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserInterface()

if __name__ == "__main__":
    UserLogin()