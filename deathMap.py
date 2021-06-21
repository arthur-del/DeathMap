import requests
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.transforms as transf
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

summoner_name = "Sc2Troller"
api_key = "RGAPI-933e7138-36fb-4fea-8ebb-c67d26e91806"
player_id = "oSK_VvGus_hg2SeP91HnRs2iVJL5pzJyEIpHO2TIKPk5Af1gH0Kb_tG1O77oN47Ri8xwIq_h9s0g-Q"
match_id = "NA1_3912809239"

def getPlayerId(name,api): #returns puuid
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "/?api_key="+api
    response = requests.get(url)
    return response.json()["puuid"]

def getMatchHistory(player_id, api): #returns array of 20 game ids
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+player_id+"/ids?start=0&count=20&api_key="+api
    response = requests.get(url)
    return response.json()

def getMatchTimeline(match_id, api):
  url = "https://americas.api.riotgames.com/lol/match/v5/matches/"+match_id+"/timeline"+ "/?api_key="+api
  response = requests.get(url)
  return response.json()

  #Nested loops to access all champion kills
def getPlayerDeathsCoordinate(timeline, victim_id):
  kill = 0
  alessandro_deaths = []
  
  for count, frame in enumerate(timeline['info']['frames']):
    #print(count, frame)
    for count2, event in enumerate(timeline['info']['frames'][count]['events']):
      #print(count2, event) 
        if (event['type'] == 'CHAMPION_KILL'):
          if (event['victimId'] == victim_id):
            kill = kill + 1
            alessandro_deaths.append(event['position'])
  return alessandro_deaths


timeline = getMatchTimeline(match_id, api_key)
victim_id = 1 +timeline['metadata']['participants'].index(player_id) # get alessandro's current game id

print(getPlayerDeathsCoordinate(timeline, victim_id))


death_array = getPlayerDeathsCoordinate(timeline, victim_id)
colors = '#FFA500'
ys = [x['x'] for x in death_array]
xs = [x['y'] for x in death_array]
plt.scatter(ys, xs, c=colors, s=100, zorder=1)
img = plt.imread('resources/lol_minimap.png')
imgplot = plt.imshow(img)
plt.title("Death Map")
plt.xlim([-570, 15220])
plt.ylim([-420, 14980])


ext = [-420.00, 15220.00, -570.00, 15220.00]
plt.imshow(img, zorder=0, extent=ext)

aspect=img.shape[0]/float(img.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
plt.gca().set_aspect(aspect)

plt.show()

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(10)
plt.show()