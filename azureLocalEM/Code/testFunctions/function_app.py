import azure.functions as func
import logging
import ujson as json
import pyodbc
import sys

sys.path.append('azureLocalEm/Code/functionActions')



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
        
        # Process the JSON data here as needed
        # You can access individual fields using json_data['field_name']
        logging.info(f"Received JSON data: {json_data}")
        for item in json_data['patientInfo']:
            logging.info(f"Item: {item}")  
        return func.HttpResponse("JSON data processed successfully.", status_code=200)
    except Exception as e:
        logging.info("Error processing JSON data.")
        logging.error(str(e))
        return func.HttpResponse(
            "Error processing JSON data.",
            status_code=500
        )
