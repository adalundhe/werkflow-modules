import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)


class AWSs3PartResponse(BaseModel):
    PartNumber: StrictInt
    LastModified: datetime.datetime
    ETag: StrictStr
    Size: StrictInt
    ChecksumCRC32: StrictStr
    ChecksumCRC32C: StrictStr
    ChecksumSHA1: StrictStr
    ChecksumSHA256: StrictStr