import datetime
from typing import Dict, Literal
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
)
from .aws_s3_streaming_body import AWSS3StreamingBody


class AWSS3GetObjectResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Body: AWSS3StreamingBody | None = None
    DeleteMarker: StrictBool | None = None
    AcceptRanges: StrictStr | None = None
    Expiration: StrictStr | None = None
    Restore: StrictStr | None = None
    LastModified: datetime.datetime | None = None
    ContentLength: StrictInt | None = None
    ETag: StrictStr | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    MissingMeta: StrictInt | None = None
    VersionId: StrictStr | None = None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentRange: StrictStr | None = None
    ContentType: StrictStr | None = None
    Expires: datetime.datetime | None = None
    WebsiteRedirectLocation: StrictStr | None = None
    ServerSideEncryption: Literal['AES256', 'aws:kms', 'aws:kms:dsse'] | None = None
    Metadata: Dict[StrictStr, StrictStr] | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
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
        'EXPRESS_ONEZONE',
    ] | None = None
    RequestCharged: Literal['requester'] | None = None
    ReplicationStatus: Literal[
        'COMPLETE',
        'PENDING',
        'FAILED',
        'REPLICA',
        'COMPLETED',
    ] | None = None
    PartsCount: StrictInt | None = None
    TagCount: StrictInt | None = None
    ObjectLockMode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    ObjectLockRetainUntilDate: datetime.datetime | None = None
    ObjectLockLegalHoldStatus: Literal['ON', 'OFF'] | None = None
