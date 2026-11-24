from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3GetObjectAnnotationRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    AnnotationName: StrictStr
    VersionId: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumMode: Literal['ENABLED'] | None = None
