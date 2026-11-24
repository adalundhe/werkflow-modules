from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3DeleteObjectAnnotationRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    AnnotationName: StrictStr
    VersionId: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ObjectIfMatch: StrictStr | None = None
