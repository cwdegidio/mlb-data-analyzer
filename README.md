# MLB Data Analyzer

This is the data analyzer for the MLB Analyzer application.
It listens for a message from a RabbitMQ service that indicates 
that data has been successfully scraped for the day. It then proceeds
to build a daily leaders board for MLB hitters based upon their OPS
(On-Base + Slugging) statistic.

Data is obtained from https://www.baseball-reference.com.

## `.env` File
Environment variables:
```text
MLB_DATA_USER=[db user name]
MLB_DATA_PW=[db user password]
MLB_DATA_IP=[db IP address]
MLB_DA_ENV=[DEV, PROD]
MLB_DA_LOG_LVL=[NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL]
MLB_MQ_URL=[messaging service URL]
MLB_DA_MET_IP=[IP address of metrics endpoints]
```

## Building Docker Image
To build the initial docker image, run:

`docker build -t mlb-data-analyzer`

## Starting the container
To run using docker compose, create an `.env` file in `/`. Then run:

`sudo docker compose --env-file /.env up`

## Metrics End Points
| End Point  | Use                                                                                                                                                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/health`  | Indicates if the analyzer is running. Returns `"status": "ok"` if the analyzer is running.                                                                                                                                                       |
| `/metrics` | Indicates how long the previous run of the analyzer took to complete (in seconds). This includes receiving the message from the data collector and running the analysis SQL query. <br/> Example: <br/>`{ "execution_time": 1.187964916229248 }` | 
