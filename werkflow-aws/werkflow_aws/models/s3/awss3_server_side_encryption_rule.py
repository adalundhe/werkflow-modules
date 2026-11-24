from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .awss3_blocked_encryption_types import AWSS3BlockedEncryptionTypes
from .awss3_server_side_encryption_by_default import AWSS3ServerSideEncryptionByDefault


class AWSS3ServerSideEncryptionRule(BaseModel):
    ApplyServerSideEncryptionByDefault: AWSS3ServerSideEncryptionByDefault | None = None
    BucketKeyEnabled: StrictBool | None = None
    BlockedEncryptionTypes: AWSS3BlockedEncryptionTypes | None = None
