from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)


class AWSs3MultipartUploadPart(BaseModel):
    ChecksumCRC32: StrictStr | None=None
    ChecksumCRC32C: StrictStr | None=None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None=None
    ChecksumSHA256: StrictStr | None=None
    ETag: StrictStr
    PartNumber: StrictInt
