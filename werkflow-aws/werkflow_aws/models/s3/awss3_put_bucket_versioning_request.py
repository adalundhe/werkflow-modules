from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_versioning_configuration import AWSS3VersioningConfiguration


class AWSS3PutBucketVersioningRequest(BaseModel):
    Bucket: StrictStr
    VersioningConfiguration: AWSS3VersioningConfiguration
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    MFA: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
