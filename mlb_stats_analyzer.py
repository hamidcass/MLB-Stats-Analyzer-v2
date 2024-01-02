import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mlbstatsapi
import time
import functools

#gets code from dictionary based off user input, used for graphing later
def offensive_stat_picker():

    stat_dict = {
        "1": "AVG",
        "2": "HR",
        "3": "RBI",
        "4": "OPS",
        "5": "OBP",
        "6": "SLG",
        "7": "H",
        "8": "R",
        "9": "BB",
        "10": "SB",
        "11": "CS",
        "12": "HBP",
        "13": "2B",
        "14": "3B",
        "15": "AB/HR",
        "16": "GP",
        "17": "AB"
    }


    os.system('cls' if os.name == 'nt' else 'clear')

    print("Choose 2 stats to compare:") 

    print("\r--[1] - Batting Average")
    print("\r--[2] - Home Runs")
    print("\r--[3] - Runs Batted In")
    print("\r--[4] - On Base Plus Slugging")
    print("\r--[5] - On Base Percentage")
    print("\r--[6] - Slugging Percentage")
    print("\r--[7] - Hits")
    print("\r--[8] - Runs")
    print("\r--[9] - Base on Balls")
    print("\r--[10] - Stolen Bases")
    print("\r--[11] - Caught Stealing")
    print("\r--[12] - Hit by Pitch")
    print("\r--[13] - Doubles")
    print("\r--[14] - Triples")
    print("\r--[15] - At Bats Per Home Run")
    print("\r--[16] - Games Played")
    print("\r--[17] - At Bats")

    valid_choice = 0
    while valid_choice == 0:
        user_choice = input("Enter your choice: ")

        if user_choice.isdigit():
            if int(user_choice) > 0 and int(user_choice) < 18:
                return stat_dict.get(user_choice)
            else:
                print("Please enter a number from 1-17")
        else:
            print("Please enter a number from 1-17")
            valid_choice = 0

def pitching_stat_picker():
    stat_dict = {

        "1": "G",
        "2": "IP",
        "3": "W",
        "4": "L",
        "5": "ERA",
        "6": "WHIP",
        "7": "SO/9",
        "8": "BB",
    }

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Choose 2 stats to compare:") 

    print("\r--[1] - Games Played")
    print("\r--[2] - Innings Pitched")
    print("\r--[3] - Wins")
    print("\r--[4] - Loses")
    print("\r--[5] - Earned Run Average")
    print("\r--[6] - Walks and Hits Per Innings Pitched")
    print("\r--[7] - Strikeouts Per Nine Innings")
    print("\r--[8] - Base on Balls")

    valid_choice = 0
    while valid_choice == 0:
        user_choice = input("Enter your choice: ")

        if user_choice.isdigit():
            if int(user_choice) > 0 and int(user_choice) < 9:
                return stat_dict.get(user_choice)
            else:
                print("Please enter a number from 1-8")
        else:
            print("Please enter a number from 1-8")
            valid_choice = 0


#convert csvs to dataframes
            
pitchers_df = pd.read_csv("all_pitchers_2023.csv")  
hitters_df = pd.read_csv("all_hitters_2023.csv")  

print("All available databases:")
print("--[1] Hitters (2023)")
print("--[2] Pitchers (2023)")


#user will choose to analyze either pitchers or hitters

valid_choice = 0
while(valid_choice == 0):

    user_choice = input("Please enter your option: ")

    if(user_choice.isdigit()):

        if int(user_choice) > 0 and int(user_choice) < 3:

            if int(user_choice) == 1:
                valid_choice = 1
            elif int(user_choice) == 2:
                valid_choice = 1


if int(user_choice) == 1:
    #offensive database
    stat_1 = offensive_stat_picker()
    stat_2 = offensive_stat_picker()

    hitters_sorted_x = hitters_df.sort_values(by=stat_1)
    hitters_sorted_y = hitters_df.sort_values(by=stat_2)
    #print(pitchers_sorted_y)
    hitters_sorted_y = hitters_sorted_y.reindex(hitters_sorted_x.index)
    plt.scatter(hitters_sorted_x[stat_1], hitters_sorted_y[stat_2])
    plt.xlabel(stat_1)
    plt.ylabel(stat_2)
    plt.show()

elif int(user_choice) == 2:
    #pitchers database
    stat_1 = pitching_stat_picker()
    stat_2 = pitching_stat_picker()

    pitchers_sorted_x = pitchers_df.sort_values(by=stat_1)
    pitchers_sorted_y = pitchers_df.sort_values(by=stat_2)
    #print(pitchers_sorted_y)
    pitchers_sorted_y = pitchers_sorted_y.reindex(pitchers_sorted_x.index)
    plt.scatter(pitchers_sorted_x[stat_1], pitchers_sorted_y[stat_2])
    plt.xlabel(stat_1)
    plt.ylabel(stat_2)
    plt.show()

























"""
#print(pitchers_df)

pitchers_sorted_x = pitchers_df.sort_values(by="ERA")
pitchers_sorted_y = pitchers_df.sort_values(by="SO/9")
print(pitchers_sorted_y)
pitchers_sorted_y = pitchers_sorted_y.reindex(pitchers_sorted_x.index)
plt.scatter(pitchers_sorted_x["ERA"], pitchers_sorted_y["SO/9"])
plt.xlabel("ERA")
plt.ylabel("SO/9")
plt.show()
"""
