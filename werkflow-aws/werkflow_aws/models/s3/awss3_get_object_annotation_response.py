from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class AWSS3GetObjectAnnotationResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    AnnotationPayload: StrictBytes | Any | None = None
    ObjectVersionId: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    ContentLength: StrictInt | None = None
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
    ReplicationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
