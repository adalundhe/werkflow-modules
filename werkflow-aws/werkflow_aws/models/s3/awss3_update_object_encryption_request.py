from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_object_encryption import AWSS3ObjectEncryption


class AWSS3UpdateObjectEncryptionRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    ObjectEncryption: AWSS3ObjectEncryption
    VersionId: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
