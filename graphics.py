import json
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd


keys = ["red_dead_redemption_2", "monster_hunter_world", "fallout_76", "marvel_spider_man", "god_of_war"]

def handle_json_load(filename):
    with open(filename) as handle:
        return json.loads(handle.read())

def generate_pie(data_array, path_file):
    labels = 'Negatifs', 'Positifs', 'Neutrals'
    explode = explode = (0.02, 0.02, 0.02)
    color = ['red', 'blue', 'grey']
    fig = plt.figure()
    plt.pie(data_array, explode = explode, labels = labels, colors = color, autopct='%1.1f%%', shadow=False, startangle=140)
    plt.axis('equal')
    fig.savefig(path_file, dpi=fig.dpi)

def generate_graph_date(data, path_file):
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.xticks(rotation=90)
    bars = []
    for item in data:
        df = pd.DataFrame.from_dict(item, orient='index', columns=['nb'])
        b = ax.bar(df.index, df['nb'], width=0.5, align='center')
        bars.append(b)
    plt.legend(bars, keys, loc='lower left')
    plt.title("Evolution du taux d'intérêt en fonction d'une periode donnée")
    fig.savefig(path_file, dpi=fig.dpi)

def generate_csv_from_json(data, path_file):
    fieldnames = ['city', 'number']
    with open(path_file, 'w', newline='') as file:
        w = csv.excel(file, fieldnames=fieldnames)
        w.writerow({'city': fieldnames[0], 'number': fieldnames[1]})
        for key, val in data.items():
            w.writerow({'city': key, 'number': val})

result_research = handle_json_load('result.json')
dict = { 
    "evolutions" : [],
    "cities" : []
}

for key in keys:
    sentiment = result_research[key]['sentiment']
    graph_sentiment_filename = key+'/sentiment.png'
    generate_pie(sentiment, graph_sentiment_filename)
    dict['evolutions'].append(result_research[key]['trends']['evolutions'])
    map_city_filename = key+'/cities.csv'
    generate_csv_from_json(result_research[key]['trends']['cities'], map_city_filename)
graph_trends_filename = 'trends.png'
generate_graph_date(dict['evolutions'], graph_trends_filename)

