from modules import modify
import os
import sys

def MODIFY():
    
    os.system('cls')

    print('#'*78)
    print('#'*22,"WELCOME TO MODIFY RECORDS SCREEN",'#'*22)
    print('#'*78)

    print('\n\n',' '*15,'SELECT OPTION TO WORK')
    print("1. Modify records in Team's DataFame")
    print("2. Modify records in Most Runs DataFame")
    print("3. Modify records in Best Batting Strike Rate DataFame")
    print("4. Modify records in Most Hundreds DataFame")
    print("5. Modify records in Most Wickets DataFame")
    print("6. Modify records in Most 5 Wickets Haul DataFame")
    print("7. Modify records in Best Economy DataFame")
    print('8. Exit')
    ch=int(input('Enter your choice :'))
    if ch==1:
        modify.mod_team()
        sys.exit()
    elif ch==2:
        modify.mod_most_runs()
        sys.exit()
    elif ch==3:
        modify.mod_best_strike_rate()
        sys.exit()
    elif ch==4:
        modify.mod_most_hundreds()
        sys.exit()
    elif ch==5:
        modify.mod_most_wickets()
        sys.exit()
    elif ch==6:
        modify.mod_5wicket_haul()
        sys.exit()
    elif ch==7:
        modify.mod_best_economy()
        sys.exit()
    elif ch==8:
        sys.exit()
    else:
        print('Invalid option')

if __name__ == "__main__":
    MODIFY()