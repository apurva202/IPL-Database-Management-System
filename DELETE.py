from modules import Delete
import os
import sys

def DELETE():
    
    os.system('cls')

    print('#'*74)
    print('#'*20,"WELCOME TO DELETE RECORDS SCREEN",'#'*20)
    print('#'*74)

    print("1. Delete Team's DataFame")
    print("2. Delete Most Runs DataFame")
    print("3. Delete Best Batting Strike Rate DataFame")
    print("4. Delete Most Hundreds DataFame")
    print("5. Delete Most Wickets DataFame")
    print("6. Delete Most 5 Wickets Haul DataFame")
    print("7. Delete Best Economy DataFame")
    print('8. Exit')

    ch=int(input("Enter your choice: "))
    if ch==1:
        Delete.del_team()
        sys.exit()
    elif ch==2:
        Delete.del_most_runs()
        sys.exit()
    elif ch==3:
        Delete.del_best_strike_rate()
        sys.exit()
    elif ch==4:
        Delete.del_most_hundreds()
        sys.exit()
    elif ch==5:
        Delete.del_most_wickets()
        sys.exit()
    elif ch==6:
        Delete.del_wicket_haul()
        sys.exit()
    elif ch==7:
        Delete.del_best_economy()
        sys.exit()
    elif ch==8:
        sys.exit()
    else:
        print('Invalid option')

if __name__ == "__main__":
    DELETE()