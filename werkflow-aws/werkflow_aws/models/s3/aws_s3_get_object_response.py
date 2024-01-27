import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
    StrictInt
)
from typing import Literal, Optional, Dict
from .aws_s3_streaming_body import AWSs3StreamingBody


class AWSs3GetObjectResponse(BaseModel):
    Body: AWSs3StreamingBody
    DeleteMarker: StrictBool
    AcceptRanges: StrictStr
    Expiration: StrictStr
    Restore: StrictStr
    LastModified: datetime.datetime
    ContentLength: StrictInt
    ETag: StrictStr
    ChecksumCRC32: StrictStr
    ChecksumCRC32C: StrictStr
    ChecksumSHA1: StrictStr
    ChecksumSHA256: StrictStr
    MissingMeta: StrictInt
    VersionId: StrictStr
    CacheControl: StrictStr
    ContentDisposition: StrictStr
    ContentEncoding: StrictStr
    ContentLanguage: StrictStr
    ContentRange: StrictStr
    ContentType: StrictStr
    Expires: datetime.datetime
    WebsiteREdirectLocation: StrictStr
    ServerSideEncryption: Literal[
        'AES256',
        'aws:kms',
        'aws:kms:dsse'
    ]
    Metadata: Dict[
        StrictStr,
        StrictStr
    ]
    SSECustomerAlgorithm: StrictStr
    SSECustomerKeyMD5: StrictStr
    SSECustomerId: StrictStr
    BucketKeyEnabled: StrictBool
    StorageClass: Literal[
        'STANDARD',
        'REDUCED_REDUNDANCY',
        'STANDARD_IA',
        'ONEZONE_IA',
        'INTELLIGENT_TIERING',
        'GLACIER',
        'DEEP_ARCHIVE',
        'OUTPOSTS',
        'GLACIER_IR',
        'SNOW',
        'EXPRESS_ONEZONE'
    ]
    ReqeustCharged: Optional[
        Literal['requester']
    ]=None
    ReplicationStatus: Literal[
        'COMPLETE',
        'PENDING',
        'FAILED',
        'REPLICA',
        'COMPLETED'
    ]=None
    PartsCount: StrictInt
    TagCount: StrictInt
    ObjectLockMode: Literal[
        'GOVERNANCE',
        'COMPLIANCE'
    ]
    ObjectLockRetainUntilDate: datetime.datetime
    ObjectLockLegalHoldStatus: Literal[
        'ON',
        'OFF'
    ]

    class Config:
        arbitrary_types_allowed=True