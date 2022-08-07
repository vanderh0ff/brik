from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('schooltime')

client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
db = client.brik

