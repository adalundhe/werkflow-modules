from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)
from typing import Literal, Optional
from .aws_s3_copy_object_result import AWSs3CopyOBjectResult


class AWSs3CopyObjectResponse(BaseModel):
    CopyObjectResult: AWSs3CopyOBjectResult | None = None
    Expiration: StrictStr | None = None
    CopySourceVersionId: StrictStr | None = None
    VersionId: StrictStr | None = None
    ServerSideEncryption: Literal['AES256', 'aws:kms', 'aws:kms:dsse'] | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    RequestCharged: Optional[
        Literal['requester']
    ]=None
