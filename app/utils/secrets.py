import os
from dotenv import load_dotenv




load_dotenv()




def getSecrets():
  secrets = {
      'MONGO_HOST': os.getenv("MONGO_HOST"),
      'MONGO_DB_NAME': os.getenv("MONGO_DB_NAME"),
      'GOOGLE_CLIENT_ID': os.getenv("GOOGLE_CLIENT_ID"),
      'GOOGLE_CLIENT_SECRET': os.getenv("GOOGLE_CLIENT_SECRET"),
      'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
      'MY_EMAIL_ADDRESS': os.getenv("MY_EMAIL_ADDRESS"),
  }
  return secrets