from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Any


class AWSs3DeleteBucketTaggingResponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, Any]