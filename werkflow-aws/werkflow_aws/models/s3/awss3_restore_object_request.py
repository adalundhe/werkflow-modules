from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_restore_request import AWSS3RestoreRequest


class AWSS3RestoreObjectRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    VersionId: StrictStr | None = None
    RestoreRequest: AWSS3RestoreRequest | None = None
    RequestPayer: Literal['requester'] | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
