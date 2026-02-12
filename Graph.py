import pandas as pd
import os
import matplotlib.pyplot as pt
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


def AnalyseMostWickets():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('WICKETS')
        pt.title('Analysis of Players with Most Wickets')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    mostwickets = pd.read_csv(get_csv_path('MostWickets.csv'))

    if ch == 1:
        names = list(mostwickets['Name'])
        Wickets = list(mostwickets['Wickets'])
        plotbar(names, Wickets)
    elif ch == 2:
        print('\n', mostwickets)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = eval(input('\nEnter the record numbers to analyse : '))
        names = list(mostwickets['Name'][data_index])
        Wickets = list(mostwickets['Wickets'][data_index])
        plotbar(names, Wickets)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')

def AnalyseMostRuns():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('RUNS')
        pt.title('Analysis of Players with Most Runs')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    MostRuns = pd.read_csv(get_csv_path('MostRuns.csv'))
    
    if ch == 1:
        names = list(MostRuns['Name'])
        runs = list(MostRuns['Runs'])
        plotbar(names, runs)
    elif ch == 2:
        print('\n', MostRuns)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = eval(input('\nEnter the record numbers to analyse : '))
        names = list(MostRuns['Name'][data_index])
        runs = list(MostRuns['Runs'][data_index])
        plotbar(names, runs)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')

def AnalyseMostHundreds():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('HUNDREDS')
        pt.title('Analysis of Players with Most Hundreds')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    mosthundreds = pd.read_csv(get_csv_path('MostHundreds.csv'))

    if ch == 1:
        names = list(mosthundreds['Name'])
        Hundreds = list(mosthundreds['100s'])
        plotbar(names, Hundreds)
    elif ch == 2:
        print('\n', mosthundreds)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = eval(input('\nEnter the record numbers to analyse : '))
        names = list(mosthundreds['Name'][data_index])
        Hundreds = list(mosthundreds['100s'][data_index])
        plotbar(names, Hundreds)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')

def AnalyseBestStrikeRate():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('STRIKERATE')
        pt.title('Analysis of Players with Best Strike Rate')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    beststrikerate = pd.read_csv(get_csv_path('BestStrikeRate.csv'))

    if ch == 1:
        names = list(beststrikerate['Name'])
        Strike_Rate = list(beststrikerate['Strike_Rate'])
        plotbar(names, Strike_Rate)
    elif ch == 2:
        print('\n', beststrikerate)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = [int(i) for i in input('\nEnter record numbers (comma-separated): ').split(',')]
        names = list(beststrikerate['Name'][data_index])
        Strike_Rate = list(beststrikerate['Strike_Rate'][data_index])
        plotbar(names, Strike_Rate)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')

def AnalyseBestEconomy():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('ECONOMY')
        pt.title('Analysis of Players with Best Economy')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    BestEconomy = pd.read_csv(get_csv_path('BestEconomy.csv'))

    if ch == 1:
        names = list(BestEconomy['Name'])
        economy = list(BestEconomy['Economy'])
        plotbar(names, economy)
    elif ch == 2:
        print('\n', BestEconomy)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = eval(input('\nEnter the record numbers to analyse : '))
        names = list(BestEconomy['Name'][data_index])
        economy = list(BestEconomy['Economy'][data_index])
        plotbar(names, economy)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')

def Analyse5WicketsHaul():
    os.system('cls')
    print('#'*78)
    print('#'*20, "WELCOME TO DATAFRAME ANALYSIS SCREEN", '#'*20)
    print('#'*78)

    def plotbar(x, y):
        pt.bar(x, y, color='orange', edgecolor='k', linewidth=1.5)
        pt.xlabel('NAMES')
        pt.ylabel('HAULS')
        pt.title('Analysis of Players with 5 Wickets Haul')
        pt.xticks(rotation=15)
        pt.grid(axis='y')
        pt.show()

    print('\n', ' '*15, 'SELECT OPTION TO ANALYSE')
    print("1. ALL")
    print("2. Specific Data")
    print("3. Exit")
    ch = int(input('Enter your choice : '))

    mosthaul = pd.read_csv(get_csv_path('MostHauls.csv'))

    if ch == 1:
        names = list(mosthaul['Name'])
        haul = list(mosthaul['5_Wickets'])
        plotbar(names, haul)
    elif ch == 2:
        print('\n', mosthaul)
        print('\nFormat : [a,b,c] here a,b,c are index number')
        data_index = [int(i) for i in input('\nEnter record numbers (comma-separated): ').split(',')]
        names = list(mosthaul['Name'][data_index])
        haul = list(mosthaul['5_Wickets'][data_index])
        plotbar(names, haul)
    elif ch == 3:
        sys.exit()
    else:
        print('Invalid option')
