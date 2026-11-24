from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ListObjectVersionsRequest(BaseModel):
    Bucket: StrictStr
    Delimiter: StrictStr | None = None
    EncodingType: Literal['url'] | None = None
    KeyMarker: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    Prefix: StrictStr | None = None
    VersionIdMarker: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    OptionalObjectAttributes: list[Literal['RestoreStatus']] | None = None
