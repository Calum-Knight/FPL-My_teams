import pymongo
import requests
import json
from pprint import pprint

#Connect to database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#connect to collection (if using MongoDB)
db = client.FPL_db

db.FPL_Fixture_Test.drop()

#API call - get the data needed

#Insert data into database

overview_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

overview_data = requests.get(overview_url).json()

# json_object = json.loads(user_data)

players_data = overview_data['elements']
fixture_list = []

for player in players_data:

    player_fixtures = {}

    player_id = player["id"]
    player_name = player["web_name"]

    player_performance_url = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'

    player_performance_data = requests.get(player_performance_url).json()

    # json_formatted_pp = json.dumps(player_performance_data, indent=2)
    

    player_fixtures = {"Player_Name" : player_name,
                       "Player_ID" : player_id,
                       "fixture_details" : {}
                       }
    
    player_fixure_list = []
    GW_List = []

    for x in range(0,len(player_performance_data["fixtures"])):

        if player_performance_data["fixtures"][x]["is_home"] == True:
            fixture_details = {                             
                "GameWeek" : player_performance_data["fixtures"][x]["event"],
                'Opponent' : player_performance_data["fixtures"][x]['team_a'],
                'Home' : player_performance_data["fixtures"][x]["is_home"],
                'difficulty' : player_performance_data["fixtures"][x]["difficulty"],
            }
        else:
            fixture_details = {                             
                "GameWeek" : player_performance_data["fixtures"][x]["event"],
                'Opponent' : player_performance_data["fixtures"][x]['team_h'],
                'Home' : player_performance_data["fixtures"][x]["is_home"],
                'difficulty' : player_performance_data["fixtures"][x]["difficulty"],
            }
        
        
        player_fixure_list.append(fixture_details)
        
    player_fixtures["fixture_details"] = player_fixure_list

    fixture_list.append(player_fixtures)

db.FPL_Fixture_Test.insert_many(fixture_list)


# league_id = 608129

# league_url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/'



# FPL_Fam_League.insert_many(
#     [
#         {

#         }
#     ]
    
# )

#Print to terminal to check working
# print("Data Uploaded")