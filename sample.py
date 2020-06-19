from nba_api.stats.static import players
headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# Get all players.
player_list = players.get_players()

for player in player_list:
    if player['full_name'] == 'LeBron James':
        bron = player

bron_id = bron['id']

from nba_api.stats.static import teams
team_dict = teams.get_teams()

for team in team_dict:
    if team['full_name'] == 'Golden State Warriors':
        GSW = team

GSW_id = team['id']

print(player_list)

#from nba_api.stats.endpoints import playergamelog
#gamelog_bron = playergamelog.PlayerGameLog(player_id=2544, season='2017', headers=headers)

#print(gamelog_bron)
