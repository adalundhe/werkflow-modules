from __future__ import annotations
import datetime
from typing import Any, Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AWSS3CopyObjectRequest(BaseModel):
    Bucket: StrictStr
    CopySource: StrictStr | dict[str, Any]
    Key: StrictStr
    ACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read', 'aws-exec-read', 'bucket-owner-read', 'bucket-owner-full-control'] | None = None
    CacheControl: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentType: StrictStr | None = None
    CopySourceIfMatch: StrictStr | None = None
    CopySourceIfModifiedSince: datetime.datetime | str | None = None
    CopySourceIfNoneMatch: StrictStr | None = None
    CopySourceIfUnmodifiedSince: datetime.datetime | str | None = None
    Expires: datetime.datetime | str | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    IfMatch: StrictStr | None = None
    IfNoneMatch: StrictStr | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
    MetadataDirective: Literal['COPY', 'REPLACE'] | None = None
    TaggingDirective: Literal['COPY', 'REPLACE'] | None = None
    AnnotationDirective: Literal['COPY', 'EXCLUDE'] | None = None
    ServerSideEncryption: Literal['AES256', 'aws:fsx', 'aws:backup', 'aws:kms', 'aws:kms:dsse'] | None = None
    StorageClass: Literal['STANDARD', 'REDUCED_REDUNDANCY', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_IR', 'SNOW', 'EXPRESS_ONEZONE', 'FSX_OPENZFS', 'FSX_ONTAP', 'AWS_BACKUP_WARM', 'AWS_BACKUP_LOW_COST_WARM'] | None = None
    WebsiteRedirectLocation: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    CopySourceSSECustomerAlgorithm: StrictStr | None = None
    CopySourceSSECustomerKey: StrictStr | None = None
    CopySourceSSECustomerKeyMD5: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
    Tagging: StrictStr | None = None
    ObjectLockMode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    ObjectLockRetainUntilDate: datetime.datetime | str | None = None
    ObjectLockLegalHoldStatus: Literal['ON', 'OFF'] | None = None
    ObjectLockEventHold: Literal['ON', 'OFF'] | None = None
    ObjectLockEventHoldDurationDays: StrictInt | None = None
    ObjectLockEventHoldDurationYears: StrictInt | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ExpectedSourceBucketOwner: StrictStr | None = None
