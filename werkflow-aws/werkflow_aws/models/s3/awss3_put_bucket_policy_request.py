from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3PutBucketPolicyRequest(BaseModel):
    Bucket: StrictStr
    Policy: StrictStr
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ConfirmRemoveSelfBucketAccess: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
