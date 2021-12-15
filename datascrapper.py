
#link of the website=https://www.indiainfoline.com/markets/nse-bse/index-stock/performance-analysis
#Database link=https://console.firebase.google.com/project/stock-a9896/firestore/data/~2FStock%20details~2F2021-12-14%2023:19:10

from bs4 import BeautifulSoup
import requests

url="https://www.indiainfoline.com/markets/nse-bse/index-stock/performance-analysis"
response=requests.get(url)
page_content=BeautifulSoup(response.content,'html.parser')
table_body=page_content.find("class"=="table-responsive")
table=table_body.find("table")
print(table)

table_rows = table.find_all("tr")[1:]
part_data = {}
for row in table_rows:
    td_name = row.find_all('td')[0].text
    td_ltp = row.find_all('td')[2].text
    td_day = row.find_all('td')[3].text
    td_week = row.find_all('td')[4].text
    td_month = row.find_all('td')[5].text
    td = {}
    td['StockName'] = td_name
    td['LTP'] = td_ltp
    td['Daily'] = td_day
    td['Week'] = td_week
    td['Month'] = td_month
    part_data[td_name] = [td_ltp,td_day,td_week,td_month]

print(part_data)

data={
    "Adani Ports":part_data['Adani Ports'],
    "Asian Paints":part_data['Asian Paints'],
    "Axis Bank":part_data['Axis Bank'],
    "Bajaj Auto":part_data['Bajaj Auto'],
    "Bajaj Finance":part_data['Bajaj Finance'],
    "Bajaj Finserv":part_data['Bajaj Finserv'],
    "B P C L":part_data['B P C L'],
    "Bharti Airtel":part_data['Bharti Airtel'],
    "Britannia Inds.":part_data['Britannia Inds.'],
    "Cipla":part_data['Cipla'],
    "Coal India":part_data['Coal India'],
    "Divis Lab.":part_data['Divis Lab.'],
    "Dr Reddys Labs":part_data['Dr Reddys Labs'],
    "Eicher Motors":part_data['Eicher Motors'],
    "Grasim Inds":part_data['Grasim Inds'],
    "HCL Technologies":part_data['HCL Technologies'],
    "HDFC Bank":part_data['HDFC Bank'],
    "HDFC Life Insur.":part_data['HDFC Life Insur.'],
    "Hero Motocorp":part_data['Hero Motocorp'],
    "Hindalco Inds.":part_data['Hindalco Inds.'],
     "Hind. Unilever":part_data['Hind. Unilever'],
     "ICICI Bank":part_data['ICICI Bank'],
     "IndusInd Bank":part_data['IndusInd Bank'],
     "Infosys":part_data['Infosys'],
     "ITC":part_data['ITC'],
     "JSW Steel":part_data['JSW Steel'],
}

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Singapore')
time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

cred = credentials.Certificate("stock-a9896-firebase-adminsdk-yezgr-2b37fc7dcf.json")
#firebase_admin.initialize_app(cred)
db = firestore.client()

def save(collection_id, document_id, data):
    db.collection(collection_id).document(document_id).set(data)

save(
    collection_id = "Stock details",
    document_id = f"{time}",
    data=data
)

