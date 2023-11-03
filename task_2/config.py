from dotenv import dotenv_values
config = dotenv_values()

CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]
STATE = config["STATE"]
SESSION_COOKIE_NAME = config['SESSION_COOKIE_NAME']