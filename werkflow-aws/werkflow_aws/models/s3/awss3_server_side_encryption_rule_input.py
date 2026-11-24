from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .awss3_blocked_encryption_types_input import AWSS3BlockedEncryptionTypesInput
from .awss3_server_side_encryption_by_default_input import AWSS3ServerSideEncryptionByDefaultInput


class AWSS3ServerSideEncryptionRuleInput(BaseModel):
    ApplyServerSideEncryptionByDefault: AWSS3ServerSideEncryptionByDefaultInput | None = None
    BucketKeyEnabled: StrictBool | None = None
    BlockedEncryptionTypes: AWSS3BlockedEncryptionTypesInput | None = None
