import azure.functions as func
import logging
import sys
import os
import json
import importlib
import pyodbc
from azure.functions import HttpRequest, HttpResponse



# Add the parent directory to the system path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

# Import db_test_upload
from functionActions import db_test_upload
from functionActions.db_test_upload import DataInsert

app = func.FunctionApp()

@app.function_name("HttpTrigger1")
@app.route("hello", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        json_data = req.get_json()
        if json_data is None:
            logging.info("No JSON data found.")
            return func.HttpResponse(
                "Please provide valid JSON data.",
                status_code=400
            )
        
        # logging.info(f"Received JSON data: {json_data}")
        DataInsert(json_data)
    except pyodbc.IntegrityError as e:
        logging.info("duplicate entry error in the database" )
        logging.error(str(e))
        return func.HttpResponse(
            "failed: duplicate entry error in the database",
            status_code=409
        )
    except pyodbc.DatabaseError as e:
        logging.info("Database error.")
        error_message = str(e)
        if "Violation of PRIMARY KEY" in error_message:
            logging.info("Duplicate entry error in the database.")
            logging.error(str(e))
            return func.HttpResponse(
                "Failed: Duplicate entry error in the database",
                status_code=409
            )
    except Exception as e:
        logging.info("Error processing JSON data.")
        logging.error(str(e))
        return func.HttpResponse(
            "Error processing JSON data.",
            status_code=500
        )
    return func.HttpResponse("JSON data processed successfully.", status_code=200)
