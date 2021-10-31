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
    img = np.asarray(image)
    img = letterbox(img, new_shape=640)[0]

        # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)
    # img = np.array(image.getdata()).reshape(image.size[0], image.size[1], 3)
    img = torch.from_numpy(img).to('cpu')
    img =  img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    pred = model(img, augment=False)[0]


 
 
    return func.HttpResponse(
             "pred",
             status_code=200
        )
