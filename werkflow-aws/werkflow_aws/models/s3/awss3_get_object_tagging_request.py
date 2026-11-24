from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3GetObjectTaggingRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    VersionId: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
