PMI Trend
========
PMI Trend is to query the Jira open tickets and calculate the PMI value, and write the value to Influx DB. Please set up the environment and fill the nessary configuration before executing this program.

# Usage 
* `git clone` this repo 
* Edit main.py to fill your user name and password and server configuration of Jira.
* Modify environment configuration of InfluxDB and the database name in influx.py
* Execute the main.py to query data from Jira and write the data 
