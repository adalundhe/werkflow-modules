from pydantic import BaseModel, StrictStr
from typing import Dict, Any


class AWSs3CreateMultipartUploadResponse(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    UploadId: StrictStr
    ResponseMetadata: Dict[StrictStr, Any]