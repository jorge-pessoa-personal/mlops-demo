from datetime import datetime
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUX_TOKEN = os.getenv("INFLUX_API_KEY")
INFLUX_ORG = os.getenv("INFLUX_ORG")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")
INFLUX_URL = os.getenv("INFLUX_URL")

def write_point(measurement, field, value, timestamp=None):
    if timestamp is None:
        timestamp = datetime.utcnow()

    with InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point(measurement).field(field, value).time(timestamp, WritePrecision.NS)
        write_api.write(INFLUX_BUCKET, INFLUX_ORG, point)

