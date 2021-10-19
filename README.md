# project-obd
Project on CouchDB

Script python import_reseau_cyclable.py crée BdD -> 127.0.0.1:5984/_utils pour Fauxton et Interface


Tutoriel queries mango: https://dotnetcodr.com/2017/06/21/introduction-to-couchdb-with-net-part-17-starting-with-mango-queries/

Exemple de query mango:
{
   "selector": {
      "fields": {
         "commune": {
            "$eq": "Toulouse"
         }
      }
   },
   "limit": 10
}

Query mango dans le terminal:
curl -d "@query.json" -X POST http://user:password@127.0.0.1:5984/reseau-cyclable/_find -H "Content-Type: application/json"
