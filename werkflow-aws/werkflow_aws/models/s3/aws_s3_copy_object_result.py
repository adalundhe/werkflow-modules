import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)


class AWSs3CopyOBjectResult(BaseModel):
    ETag: StrictStr | None = None
    LastModified: datetime.datetime | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ChecksumType: StrictStr | None = None
