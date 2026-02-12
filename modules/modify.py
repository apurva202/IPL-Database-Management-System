import os
import sys
import pandas as pd
from pathlib import Path
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

def mod_team():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Team DataFrame")

    csv_path = get_csv_path('Team.csv')
    Team = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(Team, '\n')
        n = int(input('Enter the record number to be modified: '))
        T_Name = input("\nEnter Team Name : ")
        Players = int(input("Enter Total number of Players : "))
        Captain = input("Enter Captain's Name : ")
        Head_Coach = input("Enter Head Coach Name : ")
        Most_Paid = input("Enter Most Paid Player Name : ")
        Team.loc[n, :] = [T_Name, Players, Captain, Head_Coach, Most_Paid]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    Team.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in Team.csv")


def mod_most_wickets():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Most Wickets DataFrame")

    csv_path = get_csv_path('MostWickets.csv')
    MostWickets = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(MostWickets, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Bowler's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Overs = float(input("Enter Total number of Overs bowled: "))
        if len(str(Overs).split('.')[1]) > 1 or int(str(Overs).split('.')[1][0]) > 6:
            print('Invalid input')
            continue
        if int(str(Overs).split('.')[1][0]) == 6:
            Overs = float(str(Overs).split('.')[0])
        Wickets = int(input("Enter Total Wickets : "))
        Average = float(input("Enter Average : "))
        MostWickets.loc[n, :] = [Name, Matches, Overs, Wickets, Average]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    MostWickets.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in MostWickets.csv")


def mod_most_runs():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Most Runs DataFrame")

    csv_path = get_csv_path('MostRuns.csv')
    MostRuns = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(MostRuns, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Average = float(input("Enter Average : "))
        MostRuns.loc[n, :] = [Name, Matches, Innings, Runs, Average]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    MostRuns.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in MostRuns.csv")


def mod_most_hundreds():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Most Hundreds DataFrame")

    csv_path = get_csv_path('MostHundreds.csv')
    MostHundreds = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(MostHundreds, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Hundreds = float(input("Enter Total Hundreds scored : "))
        MostHundreds.loc[n, :] = [Name, Matches, Innings, Runs, Hundreds]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    MostHundreds.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in MostHundreds.csv")


def mod_best_strike_rate():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Best Batting Strike Rate DataFrame")

    csv_path = get_csv_path('BestStrikeRate.csv')
    BestStrikeRate = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(BestStrikeRate, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        StrikeRate = float(input("Enter Strike Rate : "))
        BestStrikeRate.loc[n, :] = [Name, Matches, Innings, Runs, StrikeRate]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    BestStrikeRate.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in BestStrikeRate.csv")


def mod_best_economy():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Best Economy DataFrame")

    csv_path = get_csv_path('BestEconomy.csv')
    BestEconomy = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(BestEconomy, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Bowler's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Overs = float(input("Enter Total number of Overs bowled: "))
        if len(str(Overs).split('.')[1]) > 1 or int(str(Overs).split('.')[1][0]) > 6:
            print('Invalid input')
            continue
        if int(str(Overs).split('.')[1][0]) == 6:
            Overs = float(str(Overs).split('.')[0])
        Wickets = int(input("Enter Total Wickets : "))
        Economy = float(input("Enter Economy : "))
        BestEconomy.loc[n, :] = [Name, Matches, Overs, Wickets, Economy]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    BestEconomy.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in BestEconomy.csv")


def mod_5wicket_haul():
    os.system('cls')
    print('#'*78)
    print('#'*21, "WELCOME TO MODIFY RECORDS SCREEN", '#'*23)
    print('#'*78)
    print("\nLet's Modify Records of Most 5 Wickets Hauls DataFrame")

    csv_path = get_csv_path('MostHauls.csv')
    MostHauls = pd.read_csv(csv_path)
    ch = 'y'

    while ch.lower() == 'y':
        print(MostHauls, '\n')
        n = int(input('Enter the record number to be modified: '))
        Name = input("\nEnter Bowler's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Overs = float(input("Enter Total number of Overs bowled: "))
        if len(str(Overs).split('.')[1]) > 1 or int(str(Overs).split('.')[1][0]) > 6:
            print('Invalid input')
            continue
        if int(str(Overs).split('.')[1][0]) == 6:
            Overs = float(str(Overs).split('.')[0])
        Wickets = int(input("Enter Total Wickets : "))
        fiveWickets = float(input("Enter Total 5 Wickets Hauls : "))
        MostHauls.loc[n, :] = [Name, Matches, Overs, Wickets, fiveWickets]
        ch = input('Do you want to modify more records (y/n)? ')
        os.system('cls')

    MostHauls.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record modified successfully in MostHauls.csv")
