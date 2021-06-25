import requests

## Matplotlib imports commented out, waiting to transfer visual representation of death map to frontend
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import matplotlib.transforms as transf
#from matplotlib.offsetbox import OffsetImage, AnnotationBbox


#Requires: username(string), apikey(string)
#Returns: playerID(string)
def getPlayerId(name,api):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "/?api_key="+api
    response = requests.get(url)
    return response.json()["puuid"]
  
#Requires: playerID(string), apikey(string)
#Returns: 20 matchID(array)
def getMatchHistory(player_id, api):
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+player_id+"/ids?start=0&count=20&api_key="+api
    response = requests.get(url)
    return response.json()
  
#Requires: matchID, apikey
#Returns: timeline(dict)
def getMatchTimeline(match_id, api):
  url = "https://americas.api.riotgames.com/lol/match/v5/matches/"+match_id+"/timeline"+ "/?api_key="+api
  response = requests.get(url)
  return response.json()

#Requires: timeline(dict), victimID(string)
#Returns: deathCoordinates (array of dictionaries)
def getPlayerDeathsCoordinate(timeline, victim_id):
  kill = 0
  deaths_coordinates = []
  for count, frame in enumerate(timeline['info']['frames']):
    #print(count, frame)
    for count2, event in enumerate(timeline['info']['frames'][count]['events']):
      #print(count2, event) 
        if (event['type'] == 'CHAMPION_KILL'):
          if (event['victimId'] == victim_id):
            kill = kill + 1
            deaths_coordinates.append(event['position'])
  return deaths_coordinates

#Requires: username(string)
#Returns: deathCoordinates for most recent game (array of dictionaries)
def getOneMatchDeathCoordinate(username, api_key):
  pid = getPlayerId(username, api_key)
  match_history = getMatchHistory(pid, api_key)
  match_timeline = getMatchTimeline(match_history[0],api_key) #For proto - 0 we only want 1 game timeline -- change this line for proto-1
  victim_id = 1 + match_timeline['metadata']['participants'].index(pid) #ugly code that allows to identify pid in matchtimeline 
  return getPlayerDeathsCoordinate(match_timeline, victim_id)




## The code below creates creates a death minimap using matplotlib
## When refactoring occurs this will be deleted  as the deathmap will be created in the frontend

# death_array = getPlayerDeathsCoordinate(timeline, victim_id)
# colors = '#FFA500'
# ys = [x['x'] for x in death_array]
# xs = [x['y'] for x in death_array]
# plt.scatter(ys, xs, c=colors, s=100, zorder=1)
# img = plt.imread('resources/lol_minimap.png')
# imgplot = plt.imshow(img)
# plt.title("Death Map")
# plt.xlim([-570, 15220])
# plt.ylim([-420, 14980])


# ext = [-420.00, 15220.00, -570.00, 15220.00]
# plt.imshow(img, zorder=0, extent=ext)

# aspect=img.shape[0]/float(img.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
# plt.gca().set_aspect(aspect)

# plt.show()

# f = plt.figure()
# f.set_figwidth(10)
# f.set_figheight(10)
# plt.show()