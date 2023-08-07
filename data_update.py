import pymongo
import requests
import json
from pprint import pprint

#Connect to database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#connect to collection (if using MongoDB)
db = client.FPL_db


#API call - get the data needed

#Insert data into database

player_id = 12

player_performance_url = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'

player_performance_data = requests.get(player_performance_url).json()

json_formatted_pp = json.dumps(player_performance_data, indent=2)
fixture_list = []



for x in range(0,len(player_performance_data["fixtures"])):

    if player_performance_data["fixtures"][x]["is_home"] == True:
        fixture_list.append({f'Game Week {player_performance_data["fixtures"][x]["event"]}':
                            {
                                'Opponent' : player_performance_data["fixtures"][x]['team_a'],
                                'Home' : player_performance_data["fixtures"][x]["is_home"],
                                'difficulty' : player_performance_data["fixtures"][x]["difficulty"],
                            }})
    elif  player_performance_data["fixtures"][x]["is_home"] == False:
        fixture_list.append({f'Game Week {player_performance_data["fixtures"][x]["event"]}':
                        {
                            'Opponent' : player_performance_data["fixtures"][x]['team_h'],
                            'Home' : player_performance_data["fixtures"][x]["is_home"],
                            'difficulty' : player_performance_data["fixtures"][x]["difficulty"],
                        }})
    else:
         fixture_list.append("error")

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