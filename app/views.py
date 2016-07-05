from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def get_stats_view(request):
    player = request.GET.get("player") or "Sammy Watkins"
    url = "http://nfl.com/search?query={}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    data_table = souper.find(class_="stats").attrs["href"]
    # player_url = data_table.a.attrs["href"]
    content = requests.get(data_table).text
    souper = BeautifulSoup(content, "html.parser")
    player_stats = str(souper.find(id="main-content"))

    return render(request, "index.html", {"data_table": data_table, "player": player, "player_stats": player_stats})


# def get_player_view(request):
    # player = request.GET.get("player") or "Sammy Watkins"
    # print("player")
    # player_data = get_stats(player)
    # print(player_data)
    # return render(request, "index.html", {"player_data": player_data, "player": player})
