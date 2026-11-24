from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ListObjectsRequestModel(BaseModel):
    Bucket: StrictStr
    Delimiter: StrictStr | None = None
    EncodingType: Literal['url'] | None = None
    Marker: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    Prefix: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    OptionalObjectAttributes: list[Literal['RestoreStatus']] | None = None
