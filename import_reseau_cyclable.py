import json
import couchdb

USERNAME = "admin"
PASSWORD = "password"

couch = couchdb.Server()  
couch.resource.credentials = (USERNAME, PASSWORD)
db = couch.create('reseau-cyclable')  

with open('reseau-cyclable-et-vert.json') as f:
  data = json.load(f)

for element in data:
    db.save(element['fields'])
