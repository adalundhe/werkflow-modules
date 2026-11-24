from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_instance_automated_backup import RDSDBInstanceAutomatedBackup


class RDSDeleteDBInstanceAutomatedBackupResponse(BaseModel):
    DBInstanceAutomatedBackup: RDSDBInstanceAutomatedBackup | None = None
    ResponseMetadata: dict[str, Any] | None = None
