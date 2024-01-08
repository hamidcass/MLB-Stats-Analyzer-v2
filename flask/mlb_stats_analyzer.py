import json
import os
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mlbstatsapi
import time
import functools
import plotly.express as px

pitchers_df = pd.read_csv("all_pitchers_2023.csv")  
hitters_df = pd.read_csv("all_hitters_2023.csv")  
hitters_df.replace(".-..", np.nan, inplace=True)




def analyze_hitting_stats(first_stat, second_stat):

    stat_dict = {
        "Batting Average": "AVG",
        "Home Runs": "HR",
        "Runs Batted In (RBI)": "RBI",
        "On Base Plus Slugging (OPS)": "OPS",
        "On Base Percentage (OPS)": "OBP",
        "Slugging Percentage (SLG)": "SLG",
        "Hits": "H",
        "Runs": "R",
        "Base On Balls (BB)": "BB",
        "Stolen Bases (SB)": "SB",
        "Caught Stealing (CS)": "CS",
        "Hit By Pitch (HBP)": "HBP",
        "Doubles": "2B",
        "Triples": "3B",
        "At Bats Per Home Run (AB/HR)": "AB/HR",
        "Games Played": "GP",
        "At Bats": "AB"
    }


    stat_1 = stat_dict.get(first_stat)
    stat_2 = stat_dict.get(second_stat)


    graph = px.scatter(hitters_df, x=stat_1, y=stat_2, template="plotly_dark", color="GP", hover_data={'Full Name': True})
    graph.update_layout(
        autosize=False,
        width=600,  # Set width
        height=400,  # Set height
        margin=dict(l=40, r=40, t=50, b=40),  # Adjust margins
        hovermode='closest',
        uirevision='True',
        scene=dict(
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=1)
    )
        
        
    )

    graph.update_xaxes(fixedrange=False)
    graph.update_yaxes(fixedrange=False)

    #graph.show(config={"scrollZoom": True})

    return graph


def analyze_pitching_stats(first_stat, second_stat):

    stat_dict = {
        "Games Played (G)": "G",
        "Innings Pitched (IP)": "IP",
        "Wins (W)": "W",
        "Losses (L)": "L",
        "Earned Run Average (ERA)": "ERA",
        "Walks + Hits / IP (WHIP)": "WHIP",
        "Strikeouts / 9 (SO/9)": "SO/9",
        "Base On Balls (BB)": "BB",
    }


    stat_1 = stat_dict.get(first_stat)
    stat_2 = stat_dict.get(second_stat)

    graph = px.scatter(pitchers_df, x=stat_1, y=stat_2, template="plotly_dark", color="IP", hover_data={'Full Name': True})
    graph.update_layout(
        autosize=False,
        width=600,  # Set width
        height=400,  # Set height
        margin=dict(l=40, r=40, t=50, b=40),  # Adjust margins
        hovermode='closest',
        uirevision='True',
        scene=dict(
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=1)
    )
        
        
    )

    graph.update_xaxes(fixedrange=False)
    graph.update_yaxes(fixedrange=False)

    #graph.show(config={"scrollZoom": True})

    return graph

def iso_player(first_stat, second_stat, choice, player):
    #hitters dictionary
    h_stat_dict = {
        "Batting Average": "AVG",
        "Home Runs": "HR",
        "Runs Batted In (RBI)": "RBI",
        "On Base Plus Slugging (OPS)": "OPS",
        "On Base Percentage (OPS)": "OBP",
        "Slugging Percentage (SLG)": "SLG",
        "Hits": "H",
        "Runs": "R",
        "Base On Balls (BB)": "BB",
        "Stolen Bases (SB)": "SB",
        "Caught Stealing (CS)": "CS",
        "Hit By Pitch (HBP)": "HBP",
        "Doubles": "2B",
        "Triples": "3B",
        "At Bats Per Home Run (AB/HR)": "AB/HR",
        "Games Played": "GP",
        "At Bats": "AB"
    }

    #pitchers dictionary
    p_stat_dict = {
        "Games Played (G)": "G",
        "Innings Pitched (IP)": "IP",
        "Wins (W)": "W",
        "Losses (L)": "L",
        "Earned Run Average (ERA)": "ERA",
        "Walks + Hits / IP (WHIP)": "WHIP",
        "Strikeouts / 9 (SO/9)": "SO/9",
        "Base On Balls (BB)": "BB",
    }

    if(choice == "Offense"): #hitters db
        stat_1 = h_stat_dict.get(first_stat)
        stat_2 = h_stat_dict.get(second_stat)

        database = hitters_df
        colorKey = "GP"

    else:#pitchers db
        stat_1 = p_stat_dict.get(first_stat)
        stat_2 = p_stat_dict.get(second_stat)

        database = pitchers_df
        colorKey = "IP"

    graph = px.scatter(database, x=stat_1, y=stat_2, template="plotly_dark", color=colorKey, hover_data={'Full Name': True})
    graph.update_layout(
        autosize=False,
        width=600,  # Set width
        height=400,  # Set height
        margin=dict(l=40, r=40, t=50, b=40),  # Adjust margins
        hovermode='closest',
        uirevision='True',
        scene=dict(
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=1)
    )
        
        
    )

    graph.update_xaxes(fixedrange=False)
    graph.update_yaxes(fixedrange=False)
 
    #lower opacity of all players
    graph.update_traces(marker=dict(opacity=0.1), selector=dict(type='scatter', mode='markers'))

    #highlight the chosen player if a match is found
    player_searched = database["Full Name"].str.contains(player, case=False)
   
    if player_searched.any():

        #locate all values in row of found player
        player_row = database.loc[database['Full Name'] == player.title()]
        name = player_row["Full Name"].values[0]
        x = player_row[stat_1].values[0]
        y = player_row[stat_2].values[0]
        
        #add a new marker for player
        graph.add_scatter(x=[x], y=[y],marker=dict(
                    color='red',
                    size=10
                ),
               name=name)
        
        #print (index)
        #name = graph.data['customdata'][index][0] 
        #print(graph.data[0]['customdata'][index])  
       
        #graph.data[0]['customdata'][index].marker.opacity = 1
        
        
    else:
        graph.update_traces(marker=dict(opacity=1), selector=dict(type='scatter', mode='markers'))

    return graph

    
