from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_access_control_policy import AWSS3AccessControlPolicy


class AWSS3PutBucketAclRequest(BaseModel):
    Bucket: StrictStr
    ACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read'] | None = None
    AccessControlPolicy: AWSS3AccessControlPolicy | None = None
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWrite: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
