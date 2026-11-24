from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Dict, Literal


class AWSS3HeadObjectResponse(BaseModel):
    DeleteMarker: StrictBool | None = None
    AcceptRanges: StrictStr | None = None
    Expiration: StrictStr | None = None
    Restore: StrictStr | None = None
    ArchiveStatus: StrictStr | None = None
    LastModified: datetime.datetime | None = None
    ContentLength: StrictInt | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ETag: StrictStr | None = None
    MissingMeta: StrictInt | None = None
    VersionId: StrictStr | None = None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentType: StrictStr | None = None
    Expires: datetime.datetime | None = None
    WebsiteRedirectLocation: StrictStr | None = None
    ServerSideEncryption: StrictStr | None = None
    Metadata: Dict[StrictStr, StrictStr] | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    StorageClass: StrictStr | None = None
    RequestCharged: Literal['requester'] | None = None
    ReplicationStatus: StrictStr | None = None
    PartsCount: StrictInt | None = None
    ObjectLockMode: StrictStr | None = None
    ObjectLockRetainUntilDate: datetime.datetime | None = None
    ObjectLockLegalHoldStatus: StrictStr | None = None
