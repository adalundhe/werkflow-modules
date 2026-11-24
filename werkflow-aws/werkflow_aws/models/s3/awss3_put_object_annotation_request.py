from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class AWSS3PutObjectAnnotationRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Bucket: StrictStr
    Key: StrictStr
    AnnotationName: StrictStr
    AnnotationPayload: StrictBytes | BinaryIO | StrictStr
    VersionId: StrictStr | None = None
    ObjectIfMatch: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ChecksumSHA512: StrictStr | None = None
    ChecksumMD5: StrictStr | None = None
    ChecksumXXHASH64: StrictStr | None = None
    ChecksumXXHASH3: StrictStr | None = None
    ChecksumXXHASH128: StrictStr | None = None
    ContentMD5: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
