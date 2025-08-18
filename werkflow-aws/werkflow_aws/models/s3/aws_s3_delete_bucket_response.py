from pydantic import BaseModel, StrictStr, JsonValue
from typing import Dict


class AWSS3DeleteBucketReponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, JsonValue]