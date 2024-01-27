from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)

from typing import Literal, Optional


class AWSs3PutObjectResponse(BaseModel):
    Expiration: StrictStr
    ETag: StrictStr
    ChecksumCRC32: StrictStr
    ChecksumCRC32C: StrictStr
    ChecksumSHA1: StrictStr
    ChecksumSHA256: StrictStr
    ServerSideEncryption: Literal[
        'AES256',
        'aws:kms',
        'aws:kms:dsse'
    ]
    VersionId: StrictStr
    SSECustomerAlgorithm: StrictStr
    SSDCustomerMD5: StrictStr
    SSEKMSKeyId: Optional[StrictStr]=None
    SSEKMSEncryptionContext: Optional[StrictStr]=None
    BucketKeyEnabled: StrictBool
    RequestCharged: Optional[
        Literal['requester']
    ]=None