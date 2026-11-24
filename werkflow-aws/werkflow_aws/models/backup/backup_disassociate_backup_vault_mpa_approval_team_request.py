from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDisassociateBackupVaultMpaApprovalTeamRequest(BaseModel):
    BackupVaultName: StrictStr
    RequesterComment: StrictStr | None = None
