from modules import Add
import os
import sys

def ADD():

    os.system('cls')

    print('#'*78)
    print('#'*23,"WELCOME TO ADD RECORDS SCREEN",'#'*24)
    print('#'*78)

    print('\n\n',' '*15,'SELECT OPTION TO WORK')
    print("1. Add records in Team's DataFame")
    print("2. Add records in Most Runs DataFame")
    print("3. Add records in Best Batting Strike Rate DataFame")
    print("4. Add records in Most Hundreds DataFame")
    print("5. Add records in Most Wickets DataFame")
    print("6. Add records in Most 5 Wickets Haul DataFame")
    print("7. Add records in Best Economy DataFame")
    print('8. Exit')
    ch=int(input('Enter your choice :'))
    if ch==1:
        Add.AddTeam()
        sys.exit()
    elif ch==2:
        Add.AddMostRuns()
        sys.exit()
    elif ch==3:
        Add.AddBestStrike()
        sys.exit()
    elif ch==4:
        Add.AddMostHundreds()
        sys.exit()
    elif ch==5:
        Add.AddMostWickets()
        sys.exit()
    elif ch==6:
        Add.Add5WicketsHaul()
        sys.exit()
    elif ch==7:
        Add.AddBestEconomy()
        sys.exit()
    elif ch==8:
        sys.exit()
    else:
        print('Invalid option')

if __name__ == "__main__":
    ADD()