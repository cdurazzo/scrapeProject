import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# import  plotly.plotly  as py
# import plotly.graph_objs as go
seatgeek = pd.read_csv('c:\\users\\chris\\csv files\\final_seatgeek.csv')
seatgeek.head()

#Mean price across every team
mean_price = seatgeek.Price.mean()
mean_price

#Mean for each team's home games
home_group = seatgeek.groupby('Home')
mean_home_price = home_group['Price'].mean()
mean_home_price
#Another way
home_prices = {'Team': []}
for each in seatgeek.Home.unique():
    home_prices['Team'].append((each,seatgeek[seatgeek.Home == each].Price.mean()))


#Way of getting team name and value
team_prices = []
for each in home_prices['Team']:
    team_prices.append(each[1])


#Plot of teams average
fig, ax = plt.subplots()
ax.bar(x= mean_home_price.keys(),height=mean_home_price.values)
plt.xticks(rotation='vertical')
plt.show()


#Show price differential between yankees and others
#Could easily do same for other teams, maybe standings leaders

#Yankees means vs Mets means
yankees_away = seatgeek[seatgeek.Away == 'New York Yankees']
yanks_away_mean = yankees_away.Price.mean()
yankees_home = seatgeek[seatgeek.Home == 'New York Yankees']
yanks_home_mean = yankees_home.Price.mean()


yanks_team_means = yankees_away.Price.groupby(yankees_away.Home).agg('mean')
yanks_team_means
yanks_away_teams = yankees_away.Home.unique()
yanks_away_teams

mets_away = seatgeek[seatgeek.Away == 'New York Mets']
mets_away_mean = mets_away.Price.mean()
mets_home = seatgeek[seatgeek.Home == 'New York Mets']
mets_home_mean = mets_home.Price.mean()

mets_team_means = mets_away.Price.groupby(mets_away.Home).agg('mean')
mets_team_means
mets_away_teams = mets_away.Home.unique()
mets_away_teams


#Division Leaders/tied leaders if tied
red_sox_away = seatgeek[seatgeek.Away == 'Boston Red Sox']
red_sox_away_mean = red_sox_away.Price.mean()
red_sox_away_mean
sox_team_means = red_sox_away.Price.groupby(red_sox_away.Home).agg('mean')
sox_team_mean
sox_away_teams = red_sox_away.Home.unique()

indians_away = seatgeek[seatgeek.Away == 'Cleveland Indians']
indians_away_mean = indians_away.Price.mean()
indians_team_means = indians_away.Price.groupby(indians_away.Home).agg('mean')
indians_team_means
indians_away_teams = indians_away.Home.unique()

angels_away = seatgeek[seatgeek.Away == 'Los Angeles Angels']
angels_away_mean = angels_away.Price.mean()
angels_team_means = angels_away.Price.groupby(angels_away.Home).agg('mean')
angels_team_means
angels_away_teams = angels_away.Home.unique()

astros_away = seatgeek[seatgeek.Away == 'Houston Astros']
astros_away_mean = astros_away.Price.mean()
astros_team_means = astros_away.Price.groupby(astros_away.Home).agg('mean')
astros_team_means
astros_away_teams = astros_away.Home.unique()

braves_away = seatgeek[seatgeek.Away == 'Atlanta Braves']
braves_away_mean = braves_away.Price.mean()
braves_team_means = braves_away.Price.groupby(braves_away.Home).agg('mean')
braves_team_means
braves_away_teams = braves_away.Home.unique()

brewers_away = seatgeek[seatgeek.Away == 'Milwaulkee Brewers']
brewers_away_mean = braves_away.Price.mean()
brewers_team_means = brewers_away.Price.groupby(brewers_away.Home).agg('mean')
brewers_team_means
brewers_away_teams = brewers_away.Home.unique()

dbacks_away = seatgeek[seatgeek.Away == 'Arizona Diamondbacks']
dbacks_away_mean = dbacks_away.Price.mean()
dbacks_team_means = dbacks_away.Price.groupby(dbacks_away.Home).agg('mean')
dbacks_team_means
dbacks_away_teams = dbacks_away.Home.unique()




