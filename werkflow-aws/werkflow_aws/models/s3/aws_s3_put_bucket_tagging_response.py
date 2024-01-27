from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Any


class AWSs3PutBucketTaggingResponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, Any]