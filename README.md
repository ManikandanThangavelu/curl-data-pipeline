
# CURL Crypto API

  

The application provides API to perform CRUD operations on crypto data

  
  

## Prerequisites

  

- Python 3.5 or higher with pip installed

- MongoDB installed and running

- Install the required libraries by running the below command

> pip install -r requirements.txt
  

## Environment variables

Use the below environment variables for application configuration.

-  **PORT:** Port in which the application will be running

-  **DB_HOST:** MongoDB host

-  **DB_PORT:** MongoDB port

  

## Start the application

  

Once all the configurations are completed. You can start the application by running the below command and the application will be running on the configured port.

> python app.py

  

## Accessing API

  

You can start accessing the API by sending **POST** request to the below URL

> http://locahost:{PORT}/{END_POINT}
  
  

# End points

Below are the **END_POINT** that are supported

| END_POINT | Description | Input Data |
|--|--|--|
| load_data | Reads data form the input data location **data/fetchTickers.json** and loads the data in DB | None |
| insert_data | Inserts the input data into DB by performing transformations | [{< Input Data >}] |
| query_data | Queries the DB with **Symbol** passed  in the input parameter | {"symbol": "< Symbol >"} |
  

## Example request

Below is an example curl request and response to get the Top 3 teams.

**Request**

> curl --location --request POST 'http://localhost:8000/query_data' \

>--header 'Content-Type: application/json' \

>--data-raw '{"symbol": "BTC/INR"}'