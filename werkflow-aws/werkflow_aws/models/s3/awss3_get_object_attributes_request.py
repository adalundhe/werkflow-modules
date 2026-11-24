from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3GetObjectAttributesRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    ObjectAttributes: list[Literal['ETag', 'Checksum', 'ObjectParts', 'StorageClass', 'ObjectSize']]
    VersionId: StrictStr | None = None
    MaxParts: StrictInt | None = None
    PartNumberMarker: StrictInt | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
