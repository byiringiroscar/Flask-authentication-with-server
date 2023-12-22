
from dotenv import load_dotenv
import redis
import os
load_dotenv()

class ApplicationConfig:
    # SECRET_KEY = 'dsssmdmskmuoerermaertsdfghjkjxcvbn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"

    # SESSION_TYPE = "redis"
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
