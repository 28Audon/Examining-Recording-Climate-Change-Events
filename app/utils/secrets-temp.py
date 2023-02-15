import os

def getSecrets():
    secrets = {
        'MONGO_HOST':'mongodb+srv://28Audon:<mwGbHL5q1abWLxcl>@cluster0.7hop0b3.mongodb.net/Examining-Recording-Climate-Change-Events-DATABASE?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'Examining-Recording-Climate-Change-Events-DATABASE',
        'GOOGLE_CLIENT_ID': '',
        'GOOGLE_CLIENT_SECRET':'',
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets