from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBInstanceAutomatedBackupRequest(BaseModel):
    DbiResourceId: StrictStr | None = None
    DBInstanceAutomatedBackupsArn: StrictStr | None = None
