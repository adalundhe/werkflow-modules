import datetime
from pydantic import BaseModel, StrictStr, StrictInt
from typing import Literal, Dict


class AWSs3UploadPartCopyRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    PartNumber: StrictInt
    UploadId: StrictStr
    CopySource:  StrictStr | Dict[
        Literal['bucket','key','version_id'],
        StrictStr,
    ] | None = None
    CopySourceIfMatch: StrictStr | None = None
    CopySourceIfModifiedSince: datetime.datetime | None = None
    CopySourceIfNoneMatch: StrictStr | None = None
    CopySourceIfUnmodifiedSince: datetime.datetime | None = None
    CopySourceRange: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    CopySourceSSECustomerAlgorithm: StrictStr | None = None
    CopySourceSSECustomerKey: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ExpectedSourceBucketOwner: StrictStr | None = None
