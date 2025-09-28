import datetime
from pydantic import BaseModel, StrictStr, StrictBool
from typing import Literal


class AWSs3CreateMultipartUploadRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    ACL:  Literal[
        'private',
        'public-read',
        'public-read-write',
        'authenticated-read',
        'aws-exec-read',
        'bucket-owner-read',
        'bucket-owner-full-control'
    ] | None = None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentType: StrictStr | None = None
    Expires: datetime.datetime | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
    ServerSideEncryption: Literal[
        'AES256',
        'aws:kms',
        'aws:kms:dsse'
    ] | None = None
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
    ] | None = None
    WebsiteRedirectLocation: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    RequestPayer: StrictStr | None = None
    Tagging: StrictStr | None = None
    ObjectLockMode: Literal[
        'GOVERNANCE',
        'COMPLIANCE'
    ] | None = None
    ObjectLockRetainUntilDate: datetime.datetime | None = None
    ObjectLockLegalHoldStatus: Literal[
        'ON',
        'OFF'
    ] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumAlgorithm: Literal[
        'CRC32',
        'CRC32C',
        'SHA1',
        'SHA256'
    ] | None = None
    ChecksumType: Literal["COMPOSITE", "FULL_OBJECT"] | None = None
