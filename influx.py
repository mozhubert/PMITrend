# -*- coding: utf8 -*-
from influxdb import InfluxDBClient

def writeDB(createdate,value,group):
    Influx_server ='[Server Address]'
    Influx_account = '[Accout]'
    Influx_pwd = '[password]'
    Database = '[Database Name]'

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

    client = InfluxDBClient(Influx_server, 8086, Influx_account, Influx_pwd, Database)
    client.write_points(json_body)
