import azure.functions as func
import logging
import sys
import os
import json
import importlib
from azure.functions import HttpRequest, HttpResponse



# Add the parent directory to the system path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

# Import db_test_upload
from functionActions import db_test_upload
from functionActions.db_test_upload import DataInsert
<<<<<<< HEAD

=======
def main():
    importlib.reload(db_test_upload)
    if 'db_test_upload' in globals():
        print('db_test_upload is in globals')
    else:
        print('db_test_upload is not in globals')
    filepath = os.path.join(parent_dir, 'Data', 'jsonEXAMPLE.json')
    with open(filepath, 'r') as f:
        json_data = json.load(f)
        DataInsert(json_data)
>>>>>>> azurefunctions_helperfunctions

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
        print(f"Received type of data: {type(json_data)}")
        DataInsert(json_data)
        logging.info("JSON data processed successfully.")
        return func.HttpResponse("JSON data processed successfully.", status_code=200)
    except Exception as e:
        logging.info("Error processing JSON data.")
        logging.error(str(e))
        return func.HttpResponse(
            "Error processing JSON data.",
            status_code=500
<<<<<<< HEAD
        )
=======
        )
main()
>>>>>>> azurefunctions_helperfunctions
