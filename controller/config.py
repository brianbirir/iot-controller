import os
from dotenv import load_dotenv


class Config:
    """Loading of configurations from dot env file"""
    env_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_file = env_file_path + '/' + '.env'
    load_dotenv(dotenv_path=env_file)

    INFLUX_DB = os.getenv('INFLUXDB_DB')
    INFLUX_USER = os.getenv('INFLUXDB_ADMIN_USER')
    INFLUX_PASSWORD = os.getenv('INFLUXDB_ADMIN_PASSWORD')
    INFLUX_PORT = os.getenv('INFLUX_PORT')
    INFLUX_HOST = os.getenv('INFLUX_HOST')
    BROKER_PORT = os.getenv('BROKER_PORT')
    BROKER_TOPIC = os.getenv('BROKER_TOPIC')
    BROKER_QOS = os.getenv('BROKER_QOS')
    BROKER_KEEP_ALIVE = os.getenv('BROKER_KEEP_ALIVE')
    BROKER_USERNAME = os.getenv('BROKER_USERNAME')
    BROKER_PASSWORD = os.getenv('BROKER_PASSWORD')
    BROKER_URL = os.getenv('BROKER_URL')
