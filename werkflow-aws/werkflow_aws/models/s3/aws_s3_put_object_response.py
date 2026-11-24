from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)

from typing import Literal, Optional


class AWSS3PutObjectResponse(BaseModel):
    Expiration: StrictStr | None = None
    ETag: StrictStr | None = None
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ServerSideEncryption: Literal['AES256', 'aws:kms', 'aws:kms:dsse'] | None = None
    VersionId: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    SSEKMSKeyId: Optional[StrictStr]=None
    SSEKMSEncryptionContext: Optional[StrictStr]=None
    BucketKeyEnabled: StrictBool | None = None
    RequestCharged: Optional[
        Literal['requester']
    ]=None
