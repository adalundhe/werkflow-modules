from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_ownership_controls_input import AWSS3OwnershipControlsInput


class AWSS3PutBucketOwnershipControlsRequest(BaseModel):
    Bucket: StrictStr
    OwnershipControls: AWSS3OwnershipControlsInput
    ContentMD5: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
