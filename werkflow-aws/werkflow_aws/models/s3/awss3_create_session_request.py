from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3CreateSessionRequest(BaseModel):
    Bucket: StrictStr
    SessionMode: Literal['ReadOnly', 'ReadWrite'] | None = None
    ServerSideEncryption: Literal['AES256', 'aws:fsx', 'aws:backup', 'aws:kms', 'aws:kms:dsse'] | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
