from modules import Create
import os
import sys

def CREATE():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME CREATION SCREEN",'#'*20)
    print('#'*78)

    print('\n\n',' '*15,'SELECT OPTION TO WORK')
    print("1. Create Team's DataFame")
    print("2. Create Most Runs DataFame")
    print("3. Create Best Batting Strike Rate DataFame")
    print("4. Create Most Hundreds DataFame")
    print("5. Create Most Wickets DataFame")
    print("6. Create Most 5 Wickets Haul DataFame")
    print("7. Create Best Economy DataFame")
    print('8. Exit')
    ch=input('Enter your choice :')
    if ch=='1':
        Create.create_team_dataframe()
        sys.exit()
    elif ch=='2':
        Create.create_most_runs_dataframe()
        sys.exit()
    elif ch=='3':
        Create.create_best_strike_rate_dataframe()
        sys.exit()
    elif ch=='4':
        Create.create_most_hundreds_dataframe()
        sys.exit()
    elif ch=='5':
        Create.create_most_wickets_dataframe()
        sys.exit()
    elif ch=='6':
        Create.create_most_5_wickets_hauls_dataframe()
        sys.exit()
    elif ch=='7':
        Create.create_best_economy_dataframe()
        sys.exit()
    elif ch=='8':
        sys.exit()
    else:
        print('Invalid option')

if __name__ == "__main__":
    CREATE()