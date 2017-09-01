from stravalib.client import Client
import os 


client = Client()
authorize_url = client.authorization_url(client_id=os.environ['CLIENT_ID'], 
                                redirect_uri='http://localhost:8282/authorized')