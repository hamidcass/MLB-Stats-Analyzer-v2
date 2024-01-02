import os
import pandas as pd
import mlbstatsapi


mlb = mlbstatsapi.Mlb()

#error proof this later
chosen_year = input("Enter a year to analyze: ")

if chosen_year.isdigit():
    chosen_year = int(chosen_year)



stats = ["season"] #can add "career" to this array
groups = ["hitting", "pitching"]
params = {"season": chosen_year}

hitter_db = {
    "Full Name" : [],
    "Age" : [],
    "Current Team" : [],
    "Position" : [],
    "Throws" : [],
    "Bats" : [],
    "Height" : [],
    "Weight" : [],
    "Birth Country" : [],
    "Uniform #" : [],
    "Birthdate" : [],
   
    "AVG" : [],
    "HR" : [],
    "RBI" : [],
    "OPS" : [],
    "OBP" : [],
    "SLG" : [],
    "H" : [],
    "R" : [],
    "BB" : [],
    "SB" : [],
    "CS" : [],
    "HBP": [],
    "2B" : [],
    "3B" : [],
    "AB/HR" : [],
    "GP" : [],
    "AB" : [],
    "ID" : []

}
pitcher_db = {
    "Full Name" : [],
    "Age" : [],
    "Current Team" : [],
    "Position" : [],
    "Throws" : [],
    "Bats" : [],
    "Height" : [],
    "Weight" : [],
    "Birth Country" : [],
    "Uniform #" : [],
    "Birthdate" : [],
    
    "G" : [],
    "IP" : [],
    "W" : [],
    "L" : [],
    "ERA" : [],
    "WHIP" : [],
    "SO/9" : [],
    "BB" : [],
    "ID" : []
}

#api call - stores a list of all active players based of above parameters
all_active_players = mlb.get_people(1, **params)

print("\nCollecting stats...")

denom = len(all_active_players)
counter = 0

#iterate through all players and record bio and season stats

for player in all_active_players:
    


    #simple loading prompt
    percent = (counter/denom)*100
    print(f"\rFetching results - {counter}/{denom} ({percent:.2f}%) ", end='', flush=True)
    counter += 1

    #get bio
    if player.primaryposition.abbreviation == "P":
        #player is a pitcher
        pitcher_db["Full Name"].append(player.fullname)
        pitcher_db["Age"].append(player.currentage)
        pitcher_db["Current Team"].append(player.currentteam['id'])  #returns id (fix later)
        pitcher_db["Position"].append(player.primaryposition.abbreviation)
        pitcher_db["Throws"].append(player.pitchhand.code)
        pitcher_db["Bats"].append(player.batside.code)
        pitcher_db["Height"].append(player.height)
        pitcher_db["Weight"].append(player.weight)
        pitcher_db["Birth Country"].append(player.birthcountry)
        pitcher_db["Uniform #"].append(player.primarynumber)
        pitcher_db["Birthdate"].append(player.birthdate)
        pitcher_db["ID"].append(player.id)

    else:
        #player is a position player
        hitter_db["Full Name"].append(player.fullname)
        hitter_db["Age"].append(player.currentage)
        hitter_db["Current Team"].append(player.currentteam['id'])  #returns id (fix later)
        hitter_db["Position"].append(player.primaryposition.abbreviation)
        hitter_db["Throws"].append(player.pitchhand.code)
        hitter_db["Bats"].append(player.batside.code)
        hitter_db["Height"].append(player.height)
        hitter_db["Weight"].append(player.weight)
        hitter_db["Birth Country"].append(player.birthcountry)
        hitter_db["Uniform #"].append(player.primarynumber)
        hitter_db["Birthdate"].append(player.birthdate)
        hitter_db["ID"].append(player.id)
    
    #api call - get stats for current player  
    all_stats = mlb.get_player_stats(player.id, stats=stats, groups=groups, **params)

    hitting_stats = []
    pitching_stats = []


    #sort stats in our database
    if player.primaryposition.abbreviation == "P":
        pitching_stats = (all_stats["pitching"]["season"]).splits[0]

       
        pitcher_db["G"].append(pitching_stats.stat.gamesplayed)
        pitcher_db["IP"].append(pitching_stats.stat.inningspitched)
        pitcher_db["W"].append(pitching_stats.stat.wins)
        pitcher_db["L"].append(pitching_stats.stat.losses)
        pitcher_db["ERA"].append(pitching_stats.stat.era)
        pitcher_db["WHIP"].append(pitching_stats.stat.whip)
        pitcher_db["SO/9"].append(pitching_stats.stat.strikeoutsper9inn)
        pitcher_db["BB"].append(pitching_stats.stat.baseonballs)



    else:
        hitting_stats = (all_stats["hitting"]["season"]).splits[0]
        
        hitter_db["AVG"].append(hitting_stats.stat.avg)
        hitter_db["HR"].append(hitting_stats.stat.homeruns)
        hitter_db["RBI"].append(hitting_stats.stat.rbi)
        hitter_db["OPS"].append(hitting_stats.stat.ops)
        hitter_db["OBP"].append(hitting_stats.stat.obp)
        hitter_db["SLG"].append(hitting_stats.stat.slg)
        hitter_db["H"].append(hitting_stats.stat.hits)
        hitter_db["R"].append(hitting_stats.stat.runs)
        hitter_db["BB"].append(hitting_stats.stat.baseonballs)
        hitter_db["SB"].append(hitting_stats.stat.stolenbases)
        hitter_db["CS"].append(hitting_stats.stat.caughtstealing)
        hitter_db["HBP"].append(hitting_stats.stat.hitbypitch)
        hitter_db["2B"].append(hitting_stats.stat.doubles)
        hitter_db["3B"].append(hitting_stats.stat.triples)
        hitter_db["AB/HR"].append(hitting_stats.stat.atbatsperhomerun)
        hitter_db["GP"].append(hitting_stats.stat.gamesplayed)
        hitter_db["AB"].append(hitting_stats.stat.atbats)



#create dataframes from collected results

pitcher_df = pd.DataFrame(pitcher_db) 
hitter_df = pd.DataFrame(hitter_db)

#turn df to csv

pitcher_df.to_csv("all_pitchers_2023.csv", index=False)
hitter_df.to_csv("all_hitters_2023.csv", index=False)

