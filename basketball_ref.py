from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team, OutputType
import pandas as pd

# client.player_box_scores(day=1,month=1, year=2017, output_type=OutputType.CSV, output_file_path="./1_1_2017_box_score")
# print("PlayerBoxScores")
#
# client.players_season_totals(season_end_year=2018, output_type=OutputType.JSON, output_file_path="./season_totals")
# print("Season")
#
# client.team_box_scores(day=1,month=1, year=2017, output_type=OutputType.CSV, output_file_path="./1_1_2017_team_box_score")


file ="1_1_2017_team_box_score"
game = pd.read_csv(file)


print(game.shape)

print(list(game.columns.values))

print(game.head(5))

print(game.tail(5))

teams = game['team']

print(teams[2])

print(game.loc[2])
