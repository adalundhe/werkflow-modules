from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ListObjectAnnotationsRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    VersionId: StrictStr | None = None
    MaxAnnotationResults: StrictInt | None = None
    AnnotationPrefix: StrictStr | None = None
    ContinuationToken: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
