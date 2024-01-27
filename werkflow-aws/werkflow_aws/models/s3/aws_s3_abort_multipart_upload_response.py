from pydantic import BaseModel, StrictStr
from typing import Dict, Any


class AWSs3AbortMultipartUploadResponse(BaseModel):
    ResponseMetadata: Dict[StrictStr, Any]