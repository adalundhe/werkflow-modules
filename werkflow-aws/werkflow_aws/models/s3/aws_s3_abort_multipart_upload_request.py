from pydantic import BaseModel, StrictStr
from typing import Literal


class AWSs3AbortMultipartUploadRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    UploadId: StrictStr
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None=None