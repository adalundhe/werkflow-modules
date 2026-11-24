from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_object_lock_configuration_input import AWSS3ObjectLockConfigurationInput


class AWSS3PutObjectLockConfigurationRequest(BaseModel):
    Bucket: StrictStr
    ObjectLockConfiguration: AWSS3ObjectLockConfigurationInput | None = None
    RequestPayer: Literal['requester'] | None = None
    Token: StrictStr | None = None
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
