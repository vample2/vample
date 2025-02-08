import json
import base64
import random
import time
import itertools
import hashlib
import requests
from urllib.parse import quote_plus




def getSign(params):
    sorted_params = sorted(params.items())
    param_str = "&".join(
        f"{k}={quote_plus(json.dumps(v)) if isinstance(v, dict) else str(v)}" for k, v in sorted_params)
    print(param_str)
    key = f"{param_str}c274bac6493544b89d9c4f9d8d542b84"
    md5_hash = hashlib.md5(key.encode()).hexdigest().lower()
    print(md5_hash)
    return md5_hash
  
params = {
        'marketingId': '1881669026921459714',
        'round':"11:00",
        "s":2,
        'secretword':'开工的第一杯幸运',
        'stamp': int(time.time() * 1000),
    }
sign = getSign(params)
