import datetime
from pydantic import BaseModel, StrictStr
from typing import Dict, Any, Literal


class AWSs3UploadPartCopyResponse(BaseModel):
    CopyPartResult: Dict[
        Literal['ETag', 'LastModified'],
        StrictStr | datetime.datetime
    ]
    ResponseMetadata: Dict[StrictStr, Any]