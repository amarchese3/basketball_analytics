import requests
import json
import pandas as pd
import json
from plotly import graph_objs as go
import plotly.plotly as py




url = "https://stats.nba.com/stats/shotchartdetail"

full_string = 'https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=45&CFPARAMS=1628372&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGM&DateFrom=02%2F24%2F2019&DateTo=02%2F24%2F2019&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=1628422&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='

# querystring = {"AheadBehind":"","CFID":"45","CFPARAMS":"1628372","ClutchTime":"","Conference":"","ContextFilter":"","ContextMeasure":"FGM","DateFrom":"02%2F24%2F2019","DateTo":"02%2F24%2F2019","Division":"","EndPeriod":"10","EndRange":"28800","GROUP_ID":"","GameEventID":"","GameID":"","GameSegment":"","GroupID":"","GroupMode":"","GroupQuantity":"5","LastNGames":"0","LeagueID":"00","Location":"","Month":"0","OnOff":"","OpponentTeamID":"0","Outcome":"","PORound":"0","Period":"0","PlayerID":"1628422","PlayerID1":"","PlayerID2":"","PlayerID3":"","PlayerID4":"","PlayerID5":"","PlayerPosition":"","PointDiff":"","Position":"","RangeType":"0","RookieYear":"","Season":"2018-19","SeasonSegment":"","SeasonType":"RegularSeason","ShotClockRange":"","StartPeriod":"1","StartRange":"0","StarterBench":"","TeamID":"0","VsConference":"","VsDivision":"","VsPlayerID1":"","VsPlayerID2":"","VsPlayerID3":"","VsPlayerID4":"","VsPlayerID5":"","VsTeamID":""}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "e6632ac3-0c98-4ace-babf-daaead20f420",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Referer": "http://example.com"
}

response = requests.request("GET", full_string, timeout=10, data=payload, headers=headers)
print(response.content)
body = response.content

json = json.loads(body)

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']
print(data)
print(columns)
df = pd.DataFrame.from_records(data, columns=columns)

columns_to_drop = ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME',
                   'GAME_DATE', 'HTM', 'VTM']

df = df.drop(columns=columns_to_drop)

print(df.describe())
print(df.to_string())



missed_shot_trace = go.Scatter(
    x = df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_X'],
    y = df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_X'],
    mode = 'markers',
    name = 'Miss',
    marker={'color': 'blue', 'size':5}
)

print(missed_shot_trace)

made_shot_trace = go.Scatter(
    x = df[df['EVENT_TYPE'] == 'Made Shot']['LOC_X'],
    y = df[df['EVENT_TYPE'] == 'Made Shot']['LOC_X'],
    mode = 'markers',
    name = 'Made',
    marker={'color': 'red', 'size':5}
)

print(made_shot_trace)


data = [missed_shot_trace, made_shot_trace]

layout = go.Layout(
    title= 'Test',
    showlegend = True,
    xaxis= {'showgrid':False, 'range': [-300,300]},
    yaxis={'showgrid':False, 'range': [-100,500]},
    height = 600,
    width = 650
)

fig = go.Figure(data=data, layout=layout)

print(fig)

from matplotlib import pyplot as plt
import plotly.io as pio

# string = str(b'c:\Users\runni_000\AppData\Local\Programs\Python\Python37\python.exe')
# pio.orca.config.executable = string
py.plot(fig, filename='test_chart')


# plt.plot(fig, filename='test_chart')
pio.write_image(fig, 'foo.png')



class Data:


    def get_data(self):
        full_string='https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=45&CFPARAMS=1628372&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGM&DateFrom=02%2F24%2F2019&DateTo=02%2F24%2F2019&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=1628422&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='

        # querystring = {"AheadBehind":"","CFID":"45","CFPARAMS":"1628372","ClutchTime":"","Conference":"","ContextFilter":"","ContextMeasure":"FGM","DateFrom":"02%2F24%2F2019","DateTo":"02%2F24%2F2019","Division":"","EndPeriod":"10","EndRange":"28800","GROUP_ID":"","GameEventID":"","GameID":"","GameSegment":"","GroupID":"","GroupMode":"","GroupQuantity":"5","LastNGames":"0","LeagueID":"00","Location":"","Month":"0","OnOff":"","OpponentTeamID":"0","Outcome":"","PORound":"0","Period":"0","PlayerID":"1628422","PlayerID1":"","PlayerID2":"","PlayerID3":"","PlayerID4":"","PlayerID5":"","PlayerPosition":"","PointDiff":"","Position":"","RangeType":"0","RookieYear":"","Season":"2018-19","SeasonSegment":"","SeasonType":"RegularSeason","ShotClockRange":"","StartPeriod":"1","StartRange":"0","StarterBench":"","TeamID":"0","VsConference":"","VsDivision":"","VsPlayerID1":"","VsPlayerID2":"","VsPlayerID3":"","VsPlayerID4":"","VsPlayerID5":"","VsTeamID":""}

        payload = ""
        headers = {
            'cache-control': "no-cache",
            'Postman-Token': "e6632ac3-0c98-4ace-babf-daaead20f420",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Referer": "http://example.com"
            }

        response = requests.request("GET", full_string,timeout=10, data=payload, headers=headers)
        print(response.content)
        body = response.content
        import json
        json = json.loads(body)

        data = json['resultSets'][0]['rowSet']
        columns = json['resultSets'][0]['headers']
        print(data)
        print(columns)
        df = pd.DataFrame.from_records(data, columns=columns)

        columns_to_drop = ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'GAME_DATE', 'HTM', 'VTM', 'EVENT_TYPE']

        df = df.drop(columns=columns_to_drop)
        print(df)
    # import requests

