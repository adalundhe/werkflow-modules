from pydantic import BaseModel, StrictStr, StrictBool
from typing import Optional, Literal


class AWSs3CompleteMultipartUploadResponse(BaseModel):
    Location: StrictStr | None = None
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    Expiration: StrictStr | None = None
    ETag: StrictStr | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ServerSideEncryption: Literal['AES256', 'aws:kms', 'aws:kms:dsse'] | None = None
    VersionId: StrictStr | None = None
    SSEKMSKeyId: Optional[StrictStr] = None
    BucketKeyEnabled: StrictBool | None = None
    RequestCharged: Optional[
        Literal['requester']
    ]=None
