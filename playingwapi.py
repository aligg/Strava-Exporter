from stravalib.client import Client
import os 
from stravalib import unithelper 


client = Client()
# authorize_url = client.authorization_url(client_id=os.environ['CLIENT_ID'], 
#                                redirect_uri='http://localhost:8282/authorized')

client.access_token = os.environ['ACCESS_TOKEN']

ali = client.get_athlete()

print ali

acts = client.get_activities(limit=10)

for act in acts:
    print act.id, act.name, unithelper.miles(act.distance), act.description

#testing
#ryan = client.get_athlete(6777976)

#print ryan.city