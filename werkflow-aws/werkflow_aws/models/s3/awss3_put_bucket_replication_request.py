from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_replication_configuration import AWSS3ReplicationConfiguration


class AWSS3PutBucketReplicationRequest(BaseModel):
    Bucket: StrictStr
    ReplicationConfiguration: AWSS3ReplicationConfiguration
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    Token: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
