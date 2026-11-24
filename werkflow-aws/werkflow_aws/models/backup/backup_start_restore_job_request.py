from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BackupStartRestoreJobRequest(BaseModel):
    RecoveryPointArn: StrictStr
    Metadata: dict[StrictStr, StrictStr]
    IamRoleArn: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    ResourceType: StrictStr | None = None
    CopySourceTagsToRestoredResource: StrictBool | None = None
