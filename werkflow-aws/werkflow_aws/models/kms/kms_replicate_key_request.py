from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_tag import KMSTag


class KMSReplicateKeyRequest(BaseModel):
    KeyId: StrictStr
    ReplicaRegion: StrictStr
    Policy: StrictStr | None = None
    BypassPolicyLockoutSafetyCheck: StrictBool | None = None
    Description: StrictStr | None = None
    Tags: list[KMSTag] | None = None
