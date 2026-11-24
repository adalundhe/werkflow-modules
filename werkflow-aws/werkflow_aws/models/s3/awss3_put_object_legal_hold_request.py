from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_object_lock_legal_hold_input import AWSS3ObjectLockLegalHoldInput


class AWSS3PutObjectLegalHoldRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    LegalHold: AWSS3ObjectLockLegalHoldInput | None = None
    RequestPayer: Literal['requester'] | None = None
    VersionId: StrictStr | None = None
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
