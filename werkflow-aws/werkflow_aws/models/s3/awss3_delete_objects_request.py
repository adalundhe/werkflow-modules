from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_delete import AWSS3Delete


class AWSS3DeleteObjectsRequest(BaseModel):
    Bucket: StrictStr
    Delete: AWSS3Delete
    MFA: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    BypassGovernanceRetention: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
