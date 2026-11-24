from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudHSMModifyBackupAttributesRequest(BaseModel):
    BackupId: StrictStr
    NeverExpires: StrictBool
