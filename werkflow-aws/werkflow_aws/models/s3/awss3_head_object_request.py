from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Literal


class AWSS3HeadObjectRequest(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    IfMatch: StrictStr | None = None
    IfModifiedSince: datetime.datetime | None = None
    IfNoneMatch: StrictStr | None = None
    IfUnmodifiedSince: datetime.datetime | None = None
    Range: StrictStr | None = None
    VersionId: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    PartNumber: StrictInt | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumMode: Literal['ENABLED'] | None = None
