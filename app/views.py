from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def get_stats(player):
    url = "http://search.nfl.com/search?query={}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    data_table = souper.find(class_="stats")
    player_url = data_table.a.attrs["href"]
    content = requests.get(player_url)
    souper = BeautifulSoup(content, "html.parser")
    return data_table

def get_player_view(request):
    player = request.GET.get("player") or "Sammy Watkins"
    print("player")
    data_table = get_stats(player)
    print(data_table)
    return render(request, "index.html", {"data_table": data_table, "player": player})
