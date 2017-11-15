import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 

def get_links_to_cars():
	url = "https://en.wikipedia.org/wiki/Category:Bentley_vehicles"

	req = requests.get(url)

	soup = BeautifulSoup(req.content,'html.parser')

	div=soup.find_all('div',attrs={'class':'mw-category-group'})

	links = []
	for i in range(0,len(div)):
		for table in div[i].find_all('li'):
			links.append('https://en.wikipedia.org'+table.a['href'])

	return links 

def create_table():
	links = get_links_to_cars()
	df = pd.DataFrame()
	for link in links:
		try:
			req = requests.get(link)
			soup = BeautifulSoup(req.content,'html.parser')

			table= soup.find_all('table', attrs={'class': 'infobox hproduct'},limit=1)
			make,model=table[0].tr.text.split(' ',maxsplit=1)
			make = make.replace('\n',"")
			model = model.replace('\n',"")
			img = table[0].find_all('img')
			img = "https://"+img[0].get('src')[2:]

			year =  table[0].find_all('tr' ,limit=6)

			year = year[4].td.text
			year = year.split('–',maxsplit=1)
			if '\n' in year[0]:
				year = year.replace('\n',"")
			##year[0]
			series = pd.Series([make,model,year[0],img])
			df= df.append(series,ignore_index=True)
		except:
			pass
	df.rename(columns={0:'Make',1:'Model',2:'Release Year',3:'Image Link'},inplace=True)
	df = df.drop(df.index[17])
	df.reset_index(inplace=True)
	
	df.to_csv("bentley_cars.csv")


create_table()
		