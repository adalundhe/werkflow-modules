from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSS3PutObjectAnnotationResponse(BaseModel):
    Key: StrictStr | None = None
    AnnotationName: StrictStr | None = None
    ObjectVersionId: StrictStr | None = None
    ETag: StrictStr | None = None
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
    ChecksumType: StrictStr | None = None
    ServerSideEncryption: StrictStr | None = None
    RequestCharged: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
