import torch
import os
import json
import numpy as np


def output_fn(prediction, response_content_type):

    def numpy_values_to_float(dict):
        return_value = {}
        for key, value in dict.items():
            if(isinstance(value, np.float32)): 
                return_value[key] = float(value)
            else:
                return_value[key] = value
        return return_value
    
    if response_content_type == "application/json":
        sanitized_prediction = [numpy_values_to_float(dict) for dict in prediction]
        return json.dumps(sanitized_prediction)
    else:
        raise ValueError(f"Unsupported response content type: {response_content_type}")