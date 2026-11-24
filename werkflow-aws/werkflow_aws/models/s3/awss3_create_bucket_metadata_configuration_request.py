from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_metadata_configuration import AWSS3MetadataConfiguration


class AWSS3CreateBucketMetadataConfigurationRequest(BaseModel):
    Bucket: StrictStr
    MetadataConfiguration: AWSS3MetadataConfiguration
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
