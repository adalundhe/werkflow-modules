from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_cluster_automated_backup import RDSDBClusterAutomatedBackup


class RDSDeleteDBClusterAutomatedBackupResponse(BaseModel):
    DBClusterAutomatedBackup: RDSDBClusterAutomatedBackup | None = None
    ResponseMetadata: dict[str, Any] | None = None
