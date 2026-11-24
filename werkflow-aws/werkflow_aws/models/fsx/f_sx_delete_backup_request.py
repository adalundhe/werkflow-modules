from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteBackupRequest(BaseModel):
    BackupId: StrictStr
    ClientRequestToken: StrictStr | None = None
