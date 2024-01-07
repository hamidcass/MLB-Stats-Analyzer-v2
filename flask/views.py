#endpoints of url
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from mlb_stats_analyzer import analyze_hitting_stats, analyze_pitching_stats

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("home_page.html")

@views.route("/collect_category", methods=['POST'])
def get_user_choice():
    if request.method == 'POST':
        
        data = request.get_json()
        chosen_category = data.get('category')
        if chosen_category == "Offense":
            return render_template("offensive_stats_chooser.html")
        else: #pitching stats chosen
            return render_template("pitching_stats_chooser.html")
        
@views.route("/collect_offensive_stats", methods=['POST'])
def get_o_stats():
    if request.method == 'POST':
        
        data = request.get_json()
        stat_1 = data.get('first_stat')
        stat_2 = data.get('second_stat')
        graph = analyze_hitting_stats(stat_1, stat_2)
        graph_json = graph.to_json()

        return render_template("graph_display.html", graph_data=graph_json)
    
@views.route("/collect_pitching_stats", methods=['POST'])
def get_p_stats():
    if request.method == 'POST':
        
        data = request.get_json()
        stat_1 = data.get('first_stat')
        stat_2 = data.get('second_stat')
        graph = analyze_pitching_stats(stat_1, stat_2)
        graph_json = graph.to_json()

        return render_template("graph_display.html", graph_data=graph_json)
    

@views.route("go-to-homepage")
def go_to_homepage():
    return redirect(url_for("views.home"))
    



