from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_accelerate_configuration import AWSS3AccelerateConfiguration


class AWSS3PutBucketAccelerateConfigurationRequest(BaseModel):
    Bucket: StrictStr
    AccelerateConfiguration: AWSS3AccelerateConfiguration
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
