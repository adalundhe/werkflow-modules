from pydantic import BaseModel, StrictStr, StrictBool
from typing import Optional, Literal
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)


class AWSs3CompleteMultipartUploadResponse(BaseModel):
    Location: StrictStr
    Bucket: StrictStr
    Key: StrictStr
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
    SSEKMSKeyId: Optional[StrictStr]
    BucketKeyEnabled: StrictBool
    RequestCharged: Optional[
        Literal['requester']
    ]=None