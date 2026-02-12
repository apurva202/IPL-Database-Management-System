import pandas as pd
import os
import time
from pathlib import Path
import sys
import shutil

def get_csv_path(filename):
    user_dir = Path.home() / "IPL_Data"
    user_dir.mkdir(exist_ok=True)

    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS) / "CSV"
    else:
        base_path = Path(__file__).resolve().parent.parent / "CSV" \
            if not (Path(__file__).resolve().parent / "CSV").exists() \
            else Path(__file__).resolve().parent / "CSV"

    user_csv = user_dir / filename

    if not user_csv.exists():
        bundled_csv = base_path / filename
        if bundled_csv.exists():
            shutil.copy(bundled_csv, user_csv)

    return str(user_csv)

def ask():
    while True:
        ask = input('\nDo you want to search more results (y/n)? ')
        if ask in ('y','Y'):
            os.system('cls')
            return True
        elif ask in ('n','N'):
            return 
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def SearchTeam():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Team DataFrame\n")

    Team = pd.read_csv(get_csv_path('Team.csv'))

    while True:
        print(Team,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Team Name')
        print('2. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter Team name: ')
            results=Team[Team['T_Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def SearchMostWickets():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Most Wickets DataFrame\n")

    MostWickets = pd.read_csv(get_csv_path('MostWickets.csv'))

    while True:
        print(MostWickets,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Wickets')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter player name: ')
            results=MostWickets[MostWickets['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            min_Wickets=int(input("Enter minimum Wickets: "))
            max_Wickets=int(input("Enter maximum Wickets: "))
            results=MostWickets[(MostWickets['Wickets']>=min_Wickets) & (MostWickets['Wickets']<=max_Wickets)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found within that Wickets range.")
                if not ask(): break
        elif ch==3:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def SearchMostRuns():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Most Runs DataFrame\n")

    MostRuns = pd.read_csv(get_csv_path('MostRuns.csv'))

    while True:
        print(MostRuns,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Runs')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter player name: ')
            results=MostRuns[MostRuns['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            min_runs=int(input("Enter minimum runs: "))
            max_runs=int(input("Enter maximum runs: "))
            results=MostRuns[(MostRuns['Runs']>=min_runs) & (MostRuns['Runs']<=max_runs)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found within that runs range.")
                if not ask(): break
        elif ch==3:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def SearchMostHundreds():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Most Hundreds DataFrame\n")

    MostHundreds = pd.read_csv(get_csv_path('MostHundreds.csv'))  

    while True:
        print(MostHundreds,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Hundreds')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter player name: ')
            results=MostHundreds[MostHundreds['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            n_hundreds=int(input("Enter Number of Hundreds: "))
            results=MostHundreds[MostHundreds['100s']==n_hundreds]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with this data.")
                if not ask(): break
        elif ch==3:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def SearchBestStrikeRate():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Best Batting Strike Rate DataFrame\n")

    BestStrikeRate = pd.read_csv(get_csv_path('BestStrikeRate.csv'))

    while True:
        print(BestStrikeRate,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Strike Rate')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter player name: ')
            results=BestStrikeRate[BestStrikeRate['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            min_strikerate=float(input("Enter minimum Strike Rate: "))
            max_strikerate=float(input("Enter maximum Strike Rate: "))
            results=BestStrikeRate[(BestStrikeRate['Strike_Rate']>=min_strikerate) & (BestStrikeRate['Strike_Rate']<=max_strikerate)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found within that Strike Rate range.")
                if not ask(): break
        elif ch==3:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def SearchBestEconomy():
    os.system('cls')
    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)
    print("\nLet's Search Records in Best Economy DataFrame\n")

    BestEconomy = pd.read_csv(get_csv_path('BestEconomy.csv'))

    while True:
        print(BestEconomy,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Economy')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
        os.system('cls')
        if ch==1:
            name=input('Enter player name: ')
            results=BestEconomy[BestEconomy['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found with that name.")
                if not ask(): break
        elif ch==2:
            min_economy=float(input("Enter minimum Economy: "))
            max_economy=float(input("Enter maximum Economy: "))
            results=BestEconomy[(BestEconomy['Economy']>=min_economy) & (BestEconomy['Economy']<=max_economy)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask(): break
            else:
                print("No records found within that economy range.")
                if not ask(): break
        elif ch==3:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)

def Search5WicketsHaul():
    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Search Records in 5 Wickets Hauls DataFrame\n")

    MostHauls=pd.read_csv(get_csv_path('MostHauls.csv'))

    while True:
        print(MostHauls,'\n')
        print(' '*15,'SEARCH MENU')
        print('1. Search by Name')
        print('2. Search by Number of Hauls')
        print('3. Exit')
        ch=int(input('Enter your choice : '))
    
        os.system('cls')
    
        if ch==1:
            name=input('Enter player name: ')
            results=MostHauls[MostHauls['Name'].str.contains(name,case=False)]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask():
                    break
            else:
                print("No records found with that name.")
                if not ask():
                    break
        elif ch==2:
            n_hauls=int(input("Enter Number of Hauls: "))
            results=MostHauls[MostHauls['5_Wickets']==n_hauls]
            if not results.empty:
                print("Search Results:\n", results)
                if not ask():
                    break
            else:
                print("No records found with this data.")
                if not ask():
                    break
        elif ch==3:
            exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)