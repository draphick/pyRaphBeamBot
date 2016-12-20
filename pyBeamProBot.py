from requests import Session, codes
import json

baseapi = "https://beam.pro/api/v1"
unpw={"username": 'user', "password": 'pass'}
chatsession = Session()

channel = chatsession.get(baseapi + '/channels/user?fields=id')
channelid = channel.json()['id']



login = chatsession.post(baseapi + '/users/login', data=unpw)
# channelid = login.json()['id']
csrf_token = login.headers["X-CSRF-Token"]

print channelid
chat_response = chatsession.get(
    baseapi + "/chats/" + str(channelid),
    headers={"X-CSRF-Token": csrf_token}
)

chat_details = chat_response.json()

print chat_details['endpoints']



# https://beam.pro/api/v1
