import pandas as pd 

seatgeek = pd.read_csv('c:\\users\\chris\\csv files\\seatgeek.csv','rb', engine='python', delimiter=",")

seatgeek = seatgeek.dropna(axis=0,how='any')

seatgeek.index = seatgeek.index / 2


#teams = list(map(lambda x: x.split(' at '), seatgeek['Game']))


#split game column into workable format
teams = list(map(lambda x: x.split(' at '), seatgeek['Game']))
#Make home and away cols
away = []
for item in enumerate(teams):
    away.append((item[1][0]))

home = []
for item in enumerate(teams):
	home.append((item[1][1]))


# pattern = r"\d{1,2}\:\d{2}[amp]{2}"
# gametime = []
# time = seatgeek['Details'][100].split(' - ')[-1]
# re.search(pattern=pattern, string = time)

#Split details into workable format
time = list(map(lambda x: x.split(' - '), seatgeek['Details']))

#Put stadium in final format
#Setting needs to be split into city, date,time
stadium = []
setting = []
for key,value in enumerate(time):
    stadium.append(time[key][0])
    setting.append(time[key][1])
stadium[0]


#Remove \n from price
dollars = []
for key,value in enumerate(seatgeek['Price']):
    dollars.append(seatgeek.Price[key].replace('\n', ''))
#remove $ from price
price = []
for key,value in enumerate(dollars):
    price.append(dollars[key].replace('$',''))
#remove USD from a few values
usd_rem = []
for key,value in enumerate(price):
     usd_rem.append(price[key].replace(' USD', ''))
#Turn price from str to int
prices = []
for key,value in enumerate(usd_rem):
    prices.append(int(value))
type(prices[1000])

# Put deals into list
deals = []
for each in seatgeek['Deal Score']:
    deals.append(each)

#Putting cleaned values into new df
seat_list = pd.DataFrame({'Away': away,
                         'Home': home,
                         'Stadium': stadium,
                         'Price': prices,
                         'Deal': deals})
#seat_list.head()

final_seatgeek = seatgeek.merge(seat_list.drop_duplicates('Deal Score'),on='Deal Score')

final_seatgeek.to_csv('c:\\users\\chris\\csv files\\final_seatgeek.csv')

#Mean ticket price w/ simple hist plot
# mean_home_price = seat_list.Price.groupby(seat_list['Home']).agg('mean')
# mean_home_price.hist()

# mean_price = seat_list.Price.agg('mean')

#Split teams into divisions
# teams = ['chicago-cubs','cincinnati-reds','milwaulkee-brewers','pittsburgh-pirates','st-louis-cardinals',
# 'atlanta-braves','miami-marlins','new-york-mets','philadelphia-phillies','washington-nationals','arizona-diamondbacks',
# 'colorado-rockies','los-angeles-dodgers','san-diego-padres','san-francisco-giants','chicago-white-sox','cleveland-indians',
# 'detroit-tigers','kansas-city-royals','minnesota-twins','baltimore-orioles','boston-red-sox','new-york-yankees','tampa-bay-rays',
# 'toronto-blue-jays','houston-astros','los-angeles-angels','oakland-athletics','seattle-mariners','texas-rangers']

# al_east =['boston-red-sox','new-york-yankees','toronto-blue-jays','tampa-bay-rays','baltimore-orioles']
# al_central = ['cleveland-indians', 'minnesota-twins','detroit-tigers', 'kansas-city-royals','chicago-white-sox']
# al_west = ['houston-astros','los-angeles-angels','seattle-mariners','oakland-athletics','texas-rangers']
# nl_east = ['atlanta-braves','philadelphia-phillies','washington-nationals','new-york-mets','miami-marlins']
# nl_central = ['st-louis-cardinals','pittsburgh-pirates','chicago-cubs','milwaulkee-brewers','cincinnati-reds']
# nl_west = ['arizona-diamondbacks','colorado-rockies','san-francisco-giants','los-angeles-dodgers','san-diego-padres']


# riv_al_e = []
# riv_al_c = []
# riv_al_w = []
# riv_nl_e = []
# riv_nl_c = []
# riv_nl_w = []
# for each in seat_list:
# 	if (seat_list.home, seat_list.away) is in al_east:
# 		riv_al_e.append(seat_list[each])
# 	elif (seat_list.home, seat_list.away) is in al_central:
# 		riv_al_c.append(seat_list[each])
# 	elif (seat_list.home, seat_list.away) is in al_west:
# 		riv_al_w.append(seat_list[each])
# 	elif (seat_list.home, seat_list.away) is in nl_east:
# 		riv_nl_e.append(seat_list[each])
# 	elif (seat_list.home, seat_list.away) is in nl_central:
# 		riv_nl_c.append(seat_list[each])
# 	elif (seat_list.home, seat_list.away) is in nl_west:
# 		riv_nl_w.append(seat_list[each])
# 	else:
# 		pass



