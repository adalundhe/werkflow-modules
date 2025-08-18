import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool,
    StrictBytes
)
from typing import Dict, BinaryIO, TextIO
from .aws_s3_checksum_algorithm import AWSS3ChecksumAlgorithm
from .aws_s3_acl import AWSS3Acl
from .aws_s3_server_side_encryption import AWSS3ServerSideEncryption
from .aws_s3_storage_class import AWSS3StorageClass
from .aws_s3_object_lock_mode import AWSS3ObjectLockMode
from .aws_s3_object_lock_legal_hold_status import AWSS3ObjectLockLegalHoldStatus


class AWSS3PutObjectRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    Body: StrictBytes | BinaryIO | TextIO
    ACL: AWSS3Acl | None=None
    CacheControl: StrictStr | None = None
    ContentDisposition: StrictStr | None =None
    ContentEncoding: StrictStr | None =None
    ContentLanguage: StrictStr | None=None
    ContentLength: StrictInt | None = None
    ContentMD5: StrictStr | None = None
    ContentType: StrictStr | None = None
    ChecksumAlgorithm: AWSS3ChecksumAlgorithm | None =None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    Expires: datetime.datetime | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    Metadata: Dict[str, str] | None =None
    server_side_encryption: AWSS3ServerSideEncryption | None = None
    storage_class: AWSS3StorageClass | None =None
    WebsiteRedirectionLocation: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    Tagging: StrictStr | None = None
    ObjectLockMode: AWSS3ObjectLockMode | None = None
    ObjectLockRetainUntilDate: datetime.datetime | None = None
    ObjectLockLegalHoldStatus: AWSS3ObjectLockLegalHoldStatus | None = None
    ExpectedbucketOwner: StrictStr | None = None
