import io
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBytes,
    ConfigDict
)
from typing import Literal


class AWSs3UploadPartRequest(BaseModel):
    Body: StrictBytes | io.FileIO | io.BytesIO | io.StringIO
    Bucket: StrictStr
    Key: StrictStr
    PartNumber: StrictInt
    UploadId: StrictStr
    ContentLength: StrictInt | None = None
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal[
        'CRC32',
        'CRC32C',
        'SHA1',
        'SHA256'
    ] | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
