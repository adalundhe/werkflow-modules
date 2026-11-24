from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupAssociateBackupVaultMpaApprovalTeamRequest(BaseModel):
    BackupVaultName: StrictStr
    MpaApprovalTeamArn: StrictStr
    RequesterComment: StrictStr | None = None
