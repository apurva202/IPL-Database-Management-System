import Search
import Graph
import os
import sys
import UserLogin
import time

def ATeam():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Team DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchTeam()
        UserLogin.UserInterface()
    elif ch==2:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def AMostWickets():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Most Wickets DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchMostWickets()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.AnalyseMostWickets()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def AMostRuns():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Most Runs DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchMostRuns()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.AnalyseMostRuns()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def AMostHundreds():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Most Hundreds DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchMostHundreds()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.AnalyseMostHundreds()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def ABestStrikeRate():
    
    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Best Strike Rate DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchBestStrikeRate()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.AnalyseBestStrikeRate()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def ABestEconomy():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse Best Economy DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.SearchBestEconomy()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.AnalyseBestEconomy()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()

def A5WicketHaul():

    os.system('cls')

    print('#'*78)
    print('#'*20,"WELCOME TO DATAFRAME ANALYSIS SCREEN",'#'*20)
    print('#'*78)

    print("\nLet's Analyse 5 Wickets Haul DataFrame")

    print('\n',' '*15,'SELECT OPTION TO ANALYSE')
    print("1. Search Records")
    print("2. Study Graph")
    print("3. Exit")
    ch=int(input('Enter your choice : '))

    if ch==1:
        Search.Search5WicketsHaul()
        UserLogin.UserInterface()
    elif ch==2:
        Graph.Analyse5WicketsHaul()
        UserLogin.UserInterface()
    elif ch==3:
        sys.exit()
    else:
        os.system('cls')
        print('Invalid option')
        time.sleep(1.3)
        UserLogin.UserInterface()