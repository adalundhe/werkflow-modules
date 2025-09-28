from pydantic import BaseModel, StrictStr, StrictInt
from typing import Literal
from .aws_s3_multipart_upload import AWSs3MultipartUpload


class AWSs3CompleteMultipartUploadRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    MultipartUpload: AWSs3MultipartUpload
    UploadId: StrictStr
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ChecksumType: Literal["COMPOSITE", "FULL_OBJECT"] | None = None
    MpuObjectSize: StrictInt | None = None
    RequestPayer: Literal["requester"] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    IfMatch: StrictStr | None = None
    IfNoneMatch: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
