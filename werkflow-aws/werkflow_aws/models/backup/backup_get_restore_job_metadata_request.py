from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetRestoreJobMetadataRequest(BaseModel):
    RestoreJobId: StrictStr
