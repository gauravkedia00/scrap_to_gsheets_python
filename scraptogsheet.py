from bs4 import BeautifulSoup
from urllib.request import urlopen
import xlwt
import requests
import openpyxl
import xlrd
from xlutils.copy import copy
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

line_in_list = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=ian+fleming+the+man+with+the+golden+gun+1st%2F1st&_sacat=0&LH_TitleDesc=0&_sop=16&_osacat=0&_odkw=ian+fleming+the+man+with+the+golden+gun+1st+1st&LH_Complete=1&LH_Sold=1&LH_TitleDesc=0'
] 
books_list = ['Sheet1']

sheet = [None] * len(line_in_list)

crawler = xlwt.Workbook(encoding='utf-8', style_compression = 0)
for count,books in enumerate(books_list,0):
	sheet[count] = client.open("Scrapper_test").worksheet(books)
	

for cor,websites in enumerate(line_in_list):
	i = 2
	url = websites	
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	for price_box in soup.findAll('span', attrs={'class': 'POSITIVE'}):
		price = price_box.text.strip()
		sheet[cor].insert_row(price,i)
		i=i+1
		
