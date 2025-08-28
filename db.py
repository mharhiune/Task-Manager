from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# connect to Mongo Atlas Cluster
mongo_client = MongoClient(os.getenv("MONGO_URI"))

# Acess database
task_manager_db = mongo_client["task_manager_db"]

# Pick a collection to operate on
tasks = task_manager_db["tasks"]