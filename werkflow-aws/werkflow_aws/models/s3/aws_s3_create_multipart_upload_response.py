from pydantic import BaseModel, StrictStr
from typing import Dict, Any


class AWSs3CreateMultipartUploadResponse(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    UploadId: StrictStr | None = None
    ResponseMetadata: Dict[StrictStr, Any] | None = None
