from stravalib.client import Client
import os 
from stravalib import unithelper


client = Client()
# authorize_url = client.authorization_url(client_id=os.environ['CLIENT_ID'], 
#                                redirect_uri='http://localhost:8282/authorized')

client.access_token = os.environ['ACCESS_TOKEN']

# ali = client.get_athlete()

#print(ali)

acts = client.get_activities(before=None, after=None, limit=10)

for act in acts:
    print(act.id, act.name, unithelper.miles(act.distance), act.description)

#testing
#ryan = client.get_athlete(6777976)

#print ryan.city


# Activities can have many streams, you can request n desired stream types
types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]

streams = client.get_activity_streams(1179030205, types=types)

#  This returns initial data for start of activity via streams
# print('streams:')
# print(streams)
# print('kvs:')
# for key, value in streams.items():
#     print(key + ' has ' + str(value.original_size) + ' original data points')
#     points = value.data
#     print(points[0])