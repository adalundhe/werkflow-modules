import datetime
from typing import BinaryIO, Dict, TextIO
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictBytes,
    StrictInt,
    StrictStr,
)
from .aws_s3_acl import AWSS3Acl
from .aws_s3_checksum_algorithm import AWSS3ChecksumAlgorithm
from .aws_s3_object_lock_legal_hold_status import AWSS3ObjectLockLegalHoldStatus
from .aws_s3_object_lock_mode import AWSS3ObjectLockMode
from .aws_s3_server_side_encryption import AWSS3ServerSideEncryption
from .aws_s3_storage_class import AWSS3StorageClass


class AWSS3PutObjectRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Bucket: StrictStr
    Key: StrictStr
    Body: StrictBytes | BinaryIO | TextIO | None = None
    ACL: AWSS3Acl | None = None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None = None
    ContentEncoding: StrictStr | None = None
    ContentLanguage: StrictStr | None = None
    ContentLength: StrictInt | None = None
    ContentMD5: StrictStr | None = None
    ContentType: StrictStr | None = None
    ChecksumAlgorithm: AWSS3ChecksumAlgorithm | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    Expires: datetime.datetime | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    Metadata: Dict[str, str] | None = None
    ServerSideEncryption: AWSS3ServerSideEncryption | None = None
    StorageClass: AWSS3StorageClass | None = None
    WebsiteRedirectLocation: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    Tagging: StrictStr | None = None
    ObjectLockMode: AWSS3ObjectLockMode | None = None
    ObjectLockRetainUntilDate: datetime.datetime | None = None
    ObjectLockLegalHoldStatus: AWSS3ObjectLockLegalHoldStatus | None = None
    ExpectedBucketOwner: StrictStr | None = None
