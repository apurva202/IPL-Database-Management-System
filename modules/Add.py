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

def AddTeam():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Team DataFrame")

    csv_path = get_csv_path('Team.csv')
    Team = pd.read_csv(csv_path)

    ch = 'y'
    n = len(Team)
    while ch.lower() == 'y':
        T_Name = input("\nEnter Team Name : ")
        Players = int(input("Enter Total number of Players : "))
        Captain = input("Enter Captain's Name : ")
        Head_Coach = input("Enter Head Coach Name : ")
        Most_Paid = input("Enter Most Paid Player Name : ")
        Team.loc[n, :] = [T_Name, Players, Captain, Head_Coach, Most_Paid]
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    Team.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in Team.csv")


def AddMostWickets():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Most Wickets DataFrame")

    csv_path = get_csv_path('MostWickets.csv')
    MostWickets = pd.read_csv(csv_path)

    ch = 'y'
    n = len(MostWickets)
    while ch.lower() == 'y':
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
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    MostWickets.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in MostWickets.csv")


def AddMostRuns():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Most Runs DataFrame")

    csv_path = get_csv_path('MostRuns.csv')
    MostRuns = pd.read_csv(csv_path)

    ch = 'y'
    n = len(MostRuns)
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Average = float(input("Enter Average : "))
        MostRuns.loc[n, :] = [Name, Matches, Innings, Runs, Average]
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    MostRuns.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in MostRuns.csv")


def AddMostHundreds():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Most Hundreds DataFrame")

    csv_path = get_csv_path('MostHundreds.csv')
    MostHundreds = pd.read_csv(csv_path)

    ch = 'y'
    n = len(MostHundreds)
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Hundreds = float(input("Enter Total Hundreds scored : "))
        MostHundreds.loc[n, :] = [Name, Matches, Innings, Runs, Hundreds]
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    MostHundreds.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in MostHundreds.csv")


def AddBestStrike():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Best Batting Strike Rate DataFrame")

    csv_path = get_csv_path('BestStrikeRate.csv')
    BestStrikeRate = pd.read_csv(csv_path)

    ch = 'y'
    n = len(BestStrikeRate)
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        StrikeRate = float(input("Enter Strike Rate : "))
        BestStrikeRate.loc[n, :] = [Name, Matches, Innings, Runs, StrikeRate]
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    BestStrikeRate.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in BestStrikeRate.csv")


def AddBestEconomy():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Best Economy DataFrame")

    csv_path = get_csv_path('BestEconomy.csv')
    BestEconomy = pd.read_csv(csv_path)

    ch = 'y'
    n = len(BestEconomy)
    while ch.lower() == 'y':
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
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    BestEconomy.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in BestEconomy.csv")


def Add5WicketsHaul():
    os.system('cls')
    print('#'*78)
    print('#'*23, "WELCOME TO ADD RECORDS SCREEN", '#'*24)
    print('#'*78)
    print("\nLet's Add Records in Most 5 Wickets Hauls DataFrame")

    csv_path = get_csv_path('MostHauls.csv')
    MostHauls = pd.read_csv(csv_path)

    ch = 'y'
    n = len(MostHauls)
    while ch.lower() == 'y':
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
        n += 1
        ch = input('Do you want to add more records (y/n)? ')

    MostHauls.to_csv(csv_path, index=False)
    os.system('cls')
    print("Record added successfully in MostHauls.csv")
