from flask import Flask
from flask import request
from flask_mail import Mail, Message
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] =  False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True 
app.config['MAIL_USERNAME'] = 'rahul.lahre0835@gmail.com'
app.config['MAIL_PASSWORD'] = 'hxoaevdrxletsuwh'
app.config['MAIL_DEFAULT_SENDER'] = ('Rahul from DELL','rahul.lahre0835@gmail.com')
app.config['MAIL_MAAX_EMAILS'] = 5
app.config['MAIL_SUPRESS_SEND'] = False #similar to debug
app.config['MAIL_ASCII_ATTACHMENTS'] = False #converts file name to ASCII

cluster = MongoClient('localhost',27017)
db  = cluster["lib"]
collection = db["books"]

@app.route("/books",methods=["GET"])
def get_books():
    all_books = list(collection.find({}))
    #return  json.dumps(all_books, default=json_util.default)
    return json.dumps(all_books, sort_keys=True,indent=4, separators=(',', ': '))


@app.route("/addbook", methods=["POST"])
def add_book():

	request_payload = request.json
	book = request_payload['book']

	'''
	existing_book = collection.find({"title":book["title"]})
    if existing_book.title():
        for ex_book in existing_book:
            old_title = ex_book["title"]
     
            updated_book = addition+old_count
            collection.find_one_and_update({"Title":book["title"]}, {"$set": {"book_title": updated_book} })

	 '''
	collection.insert_one({"Title":book["Title"],
    	"Author":book["Author"],
    	"Genre":book["Genre"],
    	"Price":book["Price"],
    	"Publisher":book["Publisher"]})
	return f"added books."


@app.route("/searchbook", methods=["POST"])
def search_book():
	request_payload = request.json
	book = request_payload['book']
	
	existing_book_T = collection.find({"Title":book["Title"]})
	if existing_book_T:
		for ex_book in existing_book_T:
			return f"book found"
	else:
		for ex_book in existing_book:
			return f"book not found"


mail = Mail(app)

@app.route('/mail')
def index():
	msg = Message('hello mail server', recipients=['rahul.lahre.nitrr@gmail.com'])
	mail.send(msg)

	return f"Message has been sent"



if __name__ == "__main__":

 	app.run(debug=True)




