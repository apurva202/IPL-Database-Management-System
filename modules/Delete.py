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

def del_team():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Teams DataFrame")

    csv_path = get_csv_path('Team.csv')
    Team = pd.read_csv(csv_path)

    print(Team)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(Team.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        Team = Team.drop(n)
        Team.to_csv(csv_path, index=False)
        os.system('cls')
        print("Team's record is deleted successfully from Team.csv file")
    else:
        os.system('cls')
        print("Team's record is not deleted from Team.csv file")


def del_most_wickets():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Most Wickets DataFrame")

    csv_path = get_csv_path('MostWickets.csv')
    MostWickets = pd.read_csv(csv_path)

    print(MostWickets)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(MostWickets.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        MostWickets = MostWickets.drop(n)
        MostWickets.to_csv(csv_path, index=False)
        os.system('cls')
        print("Most Wickets's record is deleted successfully from MostWickets.csv file")
    else:
        os.system('cls')
        print("Most Wickets's record is not deleted from MostWickets.csv file")


def del_most_runs():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Most Runs DataFrame")

    csv_path = get_csv_path('MostRuns.csv')
    MostRuns = pd.read_csv(csv_path)

    print(MostRuns)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(MostRuns.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        MostRuns = MostRuns.drop(n)
        MostRuns.to_csv(csv_path, index=False)
        os.system('cls')
        print("Most Runs's record is deleted successfully from MostRuns.csv file")
    else:
        os.system('cls')
        print("Most Runs's record is not deleted from MostRuns.csv file")


def del_most_hundreds():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Most Hundreds DataFrame")

    csv_path = get_csv_path('MostHundreds.csv')
    MostHundreds = pd.read_csv(csv_path)

    print(MostHundreds)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(MostHundreds.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        MostHundreds = MostHundreds.drop(n)
        MostHundreds.to_csv(csv_path, index=False)
        os.system('cls')
        print("Most Hundreds's record is deleted successfully from MostHundreds.csv file")
    else:
        os.system('cls')
        print("Most Hundreds's record is not deleted from MostHundreds.csv file")


def del_best_strike_rate():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Batting Strike Rate DataFrame")

    csv_path = get_csv_path('BestStrikeRate.csv')
    BestStrikeRate = pd.read_csv(csv_path)

    print(BestStrikeRate)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(BestStrikeRate.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        BestStrikeRate = BestStrikeRate.drop(n)
        BestStrikeRate.to_csv(csv_path, index=False)
        os.system('cls')
        print("Batting Strike Rate's record is deleted successfully from BestStrikeRate.csv file")
    else:
        os.system('cls')
        print("Batting Strike Rate's record is not deleted from BestStrikeRate.csv file")


def del_best_economy():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Best Economy DataFrame")

    csv_path = get_csv_path('BestEconomy.csv')
    BestEconomy = pd.read_csv(csv_path)

    print(BestEconomy)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(BestEconomy.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        BestEconomy = BestEconomy.drop(n)
        BestEconomy.to_csv(csv_path, index=False)
        os.system('cls')
        print("Best Economy's record is deleted successfully from BestEconomy.csv file")
    else:
        os.system('cls')
        print("Best Economy's record is not deleted from BestEconomy.csv file")


def del_wicket_haul():
    os.system('cls')
    print('#'*74)
    print('#'*20, "WELCOME TO DELETE RECORDS SCREEN", '#'*20)
    print('#'*74)
    print("\nLet's Delete Records in Most 5 Wickets Hauls DataFrame")

    csv_path = get_csv_path('MostHauls.csv')
    MostHauls = pd.read_csv(csv_path)

    print(MostHauls)
    n = int(input('Enter the record number to be deleted: '))
    os.system('cls')
    print('The record at', n, 'is:')
    print(MostHauls.loc[n, :])
    confirm = input('Are you sure you want to delete this record permanently? (y/n): ')
    if confirm.lower() == 'y':
        MostHauls = MostHauls.drop(n)
        MostHauls.to_csv(csv_path, index=False)
        os.system('cls')
        print("Most 5 Wickets Hauls's record is deleted successfully from MostHauls.csv file")
    else:
        os.system('cls')
        print("Most 5 Wickets Hauls's record is not deleted from MostHauls.csv file")
