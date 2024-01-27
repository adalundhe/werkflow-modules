import datetime
from pydantic import (
    BaseModel,
    StrictStr
)


class AWSs3CopyOBjectResult(BaseModel):
    ETag: StrictStr
    LastModified: datetime.datetime
    ChecksumCRC32: StrictStr
    ChecksumCRC32C: StrictStr
    ChecksumSHA1: StrictStr
    ChecksumSHA256: StrictStr