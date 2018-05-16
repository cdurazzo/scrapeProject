from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

import csv



#Opens chrome through webdriver
driver = webdriver.Chrome(executable_path='C:\\Users\\Chris\\Downloads\\Selenium_unzip\\Selenium\\chromedriver')
driver.implicitly_wait(5)

csv_file = open("C:\\Users\\Chris\\CSV Files\\seatgeek.csv", "w")
writer = csv.writer(csv_file)
# #Pass in the url
# driver.get("https://seatgeek.com/")

teams = ['chicago-cubs','cincinnati-reds','milwaulkee-brewers','pittsburgh-pirates','st-louis-cardinals',
'atlanta-braves','miami-marlins','new-york-mets','philadelphia-phillies','washington-nationals','arizona-diamondbacks',
'colorado-rockies','los-angeles-dodgers','san-diego-padres','san-francisco-giants','chicago-white-sox','cleveland-indians',
'detroit-tigers','kansas-city-royals','minnesota-twins','baltimore-orioles','boston-red-sox','new-york-yankees','tampa-bay-rays',
'toronto-blue-jays','houston-astros','los-angeles-angels','oakland-athletics','seattle-mariners','texas-rangers']

team_tix = [(team+'-tickets') for team in teams]
# print(team_tix)

# for team in team_tix:
# 	print("https://seatgeek.com/"+team)

team_url_1 = [("https://seatgeek.com/"+team+"?page={}".format(1)) for team in team_tix]
team_url_2 = [("https://seatgeek.com/"+team+"?page={}".format(2)) for team in team_tix]
team_url_3 = [("https://seatgeek.com/"+team+"?page={}".format(3)) for team in team_tix]

my_dict = {}
listing_element = []
price_element = []
value_element = []
setting_element = []


#print(len(team_url)) # 30, 0-29

for team in team_url_1:
	#Opens each individual team page
	driver.get(team)
	for each in range(len(team_url_1)):
		game_tix = driver.find_elements_by_xpath('//a[@class="event-listing-title"]')
		tix = [x.get_attribute("href") for x in game_tix]
		for each in tix:
			driver.get(each)
			listing_element = (driver.find_elements_by_xpath('//div[@class="omnibox__listing__section"]'))
			price_element = driver.find_elements_by_xpath('//span[@class="Button__ButtonContents-s1a5qxwl-2 GvgGU"]')
			value_element = driver.find_elements_by_xpath('//div[@class="omnibox__listing__deal-score"]')
			matchup_element = driver.find_element_by_xpath('//div[@id="event-title-container"]')
			setting_element = driver.find_element_by_xpath('//div[@class="event-detail-words faint-words"]') 
			
			listings = [x.text for x in listing_element]
			prices = [x.text for x in price_element]
			values = [x.text for x in value_element]
			for i in range(len(listings)):

			
				my_dict['Matchup'] = matchup_element.text
				my_dict['Setting'] = setting_element.text
				my_dict['Listing'] = listings[i]
				my_dict['Price'] = prices[i]
				my_dict['Deal Score'] = values[i]

				print(my_dict)
				writer.writerow(my_dict.values())

csv_file.close()
driver.close()
			
# with open('C:\\Users\\Chris\\CSV Filesseatgeek.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in my_dict.items():
#        writer.writerow([key, value])
			