from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)
from typing import Literal, Optional
from .aws_s3_copy_object_result import AWSs3CopyOBjectResult


class AWSs3CopyObjectResponse(BaseModel):
    CopyObjectResult: AWSs3CopyOBjectResult
    Expiration: StrictStr
    CopySourceVersionId: StrictStr
    VersionId: StrictStr
    ServerSideEncryption: Literal[
        'AES256',
        'aws:kms',
        'aws:kms:dsse'
    ]
    SSECustomerAlgorithm: StrictStr
    SSECustomerKeyMD5: StrictStr
    SSEKMSKeyId: StrictStr
    SSEKMSEncryptionContext: StrictStr
    BucketKeyEnabled: StrictBool
    RequestCharged: Optional[
        Literal['requester']
    ]=None