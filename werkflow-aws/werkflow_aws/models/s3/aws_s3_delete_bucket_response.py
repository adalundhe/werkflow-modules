from pydantic import BaseModel, StrictStr
from typing import Dict, Any


class AWSs3DeleteBucketReponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, Any]