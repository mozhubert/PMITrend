# -*- coding: utf8 -*-
from influxdb import InfluxDBClient

def writeDB(createdate,value,group):
    json_body = [
        {
            "measurement":"PMI",
            "tags":{
                "Group":group
            },
            "time":createdate,
            "fields":{
                "Value":value
            }
        }
    ]

    client = InfluxDBClient('localhost', 8086, 'root', '', 'Jira')
    client.write_points(json_body)
