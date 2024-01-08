import azure.functions as func
import logging
import datetime
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name("echo_time")
@app.route(route="utctime", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response = {}
    response["timezone"] = "UTC"
    response["timestamp"] = datetime.datetime.utcnow().isoformat()
    response["format"] = "ISO 8601"
    # return func.HttpResponse(f"{datetime.datetime.utcnow()}")
    return func.HttpResponse(json.dumps(response), mimetype="application/json")