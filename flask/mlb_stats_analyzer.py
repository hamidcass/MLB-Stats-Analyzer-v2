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