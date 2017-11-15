import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 

def get_wiki_links():
	url = 'https://en.wikipedia.org/wiki/List_of_Toyota_vehicles'

	req = requests.get(url)

	soup = BeautifulSoup(req.content, 'html.parser')

	car_links = []
	#clean_links =[]
	for link in soup.find_all('ul',limit=2):
		car_links.append(link.find_all('a',attrs={'href': re.compile("^/wiki/")}))

	col_length = sum(len(x) for x in car_links)

	for x in range(0,col_length):
		link= "https://en.wikipedia.org"+car_links[1][x].get('href')
		yield link
	# 	clean_links.append(link)
	# return clean_links
			
# 	link= "https://en.wikipedia.org/"+car_links[1][0].get('href')

# req = requests.get(link)

def create_table():
	links = get_wiki_links()
	df = pd.DataFrame()

	for link in links:
		try:
			req = requests.get(link)
			soup = BeautifulSoup(req.content, 'html.parser')
			table = soup.find_all('table',{'class':"infobox hproduct"},limit=1)
			
			img = table[0].find_all('img')
			img = "https://"+img[0].get('src')[2:]
			
			name =table[0].find_all('tr',limit=1)
			make, model = name[0].text.split(" ",maxsplit=1)
			make = make.strip('\n')
			model = model.strip('\n')

			release_year = table[0].find_all('tr',limit=6)
			release_year = release_year[5].td.text
			release_year = re.match(r'[0-9]',release_year)
			release_year = release_year.string

			series = pd.Series([make,model,release_year[:4],img])
			df= df.append(series,ignore_index=True)
		except:
			pass
	df.rename(columns={0:'Make',1:'Model',2:'Release Year',3:'Image Link'},inplace=True)
	df.to_csv("toyota_cars.csv")


create_table()