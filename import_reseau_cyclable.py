import json
import couchdb

USERNAME = "admin"
PASSWORD = "password"

couch = couchdb.Server()  
couch.resource.credentials = (USERNAME, PASSWORD)

couch.delete('reseau-cyclable')
db = couch.create('reseau-cyclable')  

with open('data/reseau-cyclable-et-vert.json') as f:
  data = json.load(f)

for element in data:
    db.save(element)
