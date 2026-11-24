from __future__ import annotations
import datetime
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictInt, StrictStr


class AWSS3WriteGetObjectResponseRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    RequestRoute: StrictStr
    RequestToken: StrictStr
    Body: StrictBytes | BinaryIO | StrictStr | None = None
    StatusCode: StrictInt | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    AcceptRanges: StrictStr | None = None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentLength: StrictInt | None = None
    ContentRange: StrictStr | None = None
    ContentType: StrictStr | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ChecksumSHA512: StrictStr | None = None
    ChecksumMD5: StrictStr | None = None
    ChecksumXXHASH64: StrictStr | None = None
    ChecksumXXHASH3: StrictStr | None = None
    ChecksumXXHASH128: StrictStr | None = None
    DeleteMarker: StrictBool | None = None
    ETag: StrictStr | None = None
    Expires: datetime.datetime | StrictStr | None = None
    Expiration: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    MissingMeta: StrictInt | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
    ObjectLockMode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    ObjectLockLegalHoldStatus: Literal['ON', 'OFF'] | None = None
    ObjectLockRetainUntilDate: datetime.datetime | StrictStr | None = None
    PartsCount: StrictInt | None = None
    ReplicationStatus: Literal['COMPLETE', 'PENDING', 'FAILED', 'REPLICA', 'COMPLETED'] | None = None
    RequestCharged: Literal['requester'] | None = None
    Restore: StrictStr | None = None
    ServerSideEncryption: Literal['AES256', 'aws:fsx', 'aws:backup', 'aws:kms', 'aws:kms:dsse'] | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    StorageClass: Literal['STANDARD', 'REDUCED_REDUNDANCY', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_IR', 'SNOW', 'EXPRESS_ONEZONE', 'FSX_OPENZFS', 'FSX_ONTAP', 'AWS_BACKUP_WARM', 'AWS_BACKUP_LOW_COST_WARM'] | None = None
    TagCount: StrictInt | None = None
    VersionId: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
