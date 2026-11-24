import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)


class AWSs3PartResponse(BaseModel):
    PartNumber: StrictInt | None = None
    LastModified: datetime.datetime | None = None
    ETag: StrictStr | None = None
    Size: StrictInt | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
