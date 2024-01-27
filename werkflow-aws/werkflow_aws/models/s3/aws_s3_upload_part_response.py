from pydantic import BaseModel, StrictStr
from typing import Dict, Any


class AWSs3UploadPartResponse(BaseModel):
    ETag: StrictStr
    ResponseMetadata: Dict[StrictStr, Any]