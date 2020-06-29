import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C:\\Users\\Rahul Lahre\\Documents\\LMS1\\books.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('localhost',27017) 
Bdb = mongo_client["lib"] 
Bdb.books.drop()
header = ["Title", "Author", "Genre", "Price", "Publisher"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    Bdb.books.insert_one(row)