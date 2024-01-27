from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Any


class AWSs3PutBucketVersioningResponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, Any]