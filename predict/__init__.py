import logging
import numpy as np
import torch
import torch.nn as nn
import azure.functions as func
from models.experimental import attempt_load
from PIL import Image
import io
import base64
MODEL_RELATIVE_PATH = "../tea_leaves.pt"

def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    model_path = "/".join([str(context.function_directory), MODEL_RELATIVE_PATH])
    model = attempt_load(model_path, map_location='cpu')
    body = req.files.get('file').stream.read()
    logging.info(type(body))

    try:
        image  = Image.open(io.BytesIO(body))
       

    except Exception as ex:
        return func.HttpResponse(
               str(ex),
                status_code=400
        )
   

    # Inference

 
 
    return func.HttpResponse(
             "pred",
             status_code=200
        )
