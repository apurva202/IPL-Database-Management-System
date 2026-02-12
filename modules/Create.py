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

def create_team_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Team Details")

    Team, temp, ch, n = {}, {}, 'y', 1
    while ch.lower() == 'y':
        T_Name = input("\nEnter Team Name : ")
        Players = int(input("Enter Total number of Players : "))
        Captain = input("Enter Captain's Name : ")
        Head_Coach = input("Enter Head Coach Name : ")
        Most_Paid = input("Enter Most Paid Player Name : ")

        temp.update({
            'T_Name': T_Name,
            'Players': Players,
            'Captain': Captain,
            'Head Coach': Head_Coach,
            'Most Paid': Most_Paid
        })
        Team[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(Team).T
    csv_path = get_csv_path('Team.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Team data is successfully stored in Team.csv')


def create_most_wickets_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Most Wickets Details")

    MostWickets, temp, ch, n = {}, {}, 'y', 1
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

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Overs': Overs,
            'Wickets': Wickets,
            'Average': Average
        })
        MostWickets[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(MostWickets).T
    csv_path = get_csv_path('MostWickets.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Most Wickets data is successfully stored in MostWickets.csv')


def create_most_runs_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Most Runs Details")

    MostRuns, temp, ch, n = {}, {}, 'y', 1
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Average = float(input("Enter Average : "))

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Innings': Innings,
            'Runs': Runs,
            'Average': Average
        })
        MostRuns[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(MostRuns).T
    csv_path = get_csv_path('MostRuns.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Most Runs data is successfully stored in MostRuns.csv')


def create_most_hundreds_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Most Hundreds Details")

    MostHundreds, temp, ch, n = {}, {}, 'y', 1
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        Hundreds = float(input("Enter Total Hundreds scored : "))

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Innings': Innings,
            'Runs': Runs,
            '100s': Hundreds
        })
        MostHundreds[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(MostHundreds).T
    csv_path = get_csv_path('MostHundreds.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Most Hundreds data is successfully stored in MostHundreds.csv')


def create_best_strike_rate_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Best Batting Strike Rate Details")

    BestStrikeRate, temp, ch, n = {}, {}, 'y', 1
    while ch.lower() == 'y':
        Name = input("\nEnter Batter's Name : ")
        Matches = int(input("Enter Total number of Matches played : "))
        Innings = int(input("Enter Total number of Innings played : "))
        if Matches < Innings:
            print('Invalid input\nInnings must be ≤ Matches')
            continue
        Runs = int(input("Enter Total Runs Scored : "))
        StrikeRate = float(input("Enter Strike Rate : "))

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Innings': Innings,
            'Runs': Runs,
            'Strike_Rate': StrikeRate
        })
        BestStrikeRate[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(BestStrikeRate).T
    csv_path = get_csv_path('BestStrikeRate.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Best Batting Strike Rate data is successfully stored in BestStrikeRate.csv')


def create_best_economy_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Best Economy Details")

    BestEconomy, temp, ch, n = {}, {}, 'y', 1
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

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Overs': Overs,
            'Wickets': Wickets,
            'Economy': Economy
        })
        BestEconomy[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(BestEconomy).T
    csv_path = get_csv_path('BestEconomy.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Best Economy data is successfully stored in BestEconomy.csv')


def create_most_5_wickets_hauls_dataframe():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME CREATION SCREEN", '#'*20)
    print('#'*78)
    print("\nLet's Create DataFrame for Most 5 Wickets Hauls Details")

    MostHauls, temp, ch, n = {}, {}, 'y', 1
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

        temp.update({
            'Name': Name,
            'Matches': Matches,
            'Overs': Overs,
            'Wickets': Wickets,
            '5_Wickets': fiveWickets
        })
        MostHauls[n] = temp.copy()
        n += 1
        ch = input('Do you want to enter more records (y/n)? ')

    df = pd.DataFrame(MostHauls).T
    csv_path = get_csv_path('MostHauls.csv')
    df.to_csv(csv_path, index=False)

    os.system('cls')
    print('Most 5 Wickets Hauls data is successfully stored in MostHauls.csv')
