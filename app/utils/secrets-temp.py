import os

def getSecrets():
    secrets = {
        'MONGO_HOST':'mongodb+srv://28Audon:<password>@cluster0.7hop0b3.mongodb.net/?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'',
        'GOOGLE_CLIENT_ID': '156656430524-83s2o73ontsca6e2004valk279e1saea.apps.googleusercontent.com',
        'GOOGLE_CLIENT_SECRET':'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',
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets