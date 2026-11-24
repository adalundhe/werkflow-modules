from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_automated_backup import RDSDBClusterAutomatedBackup


class RDSDescribeDBClusterAutomatedBackupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterAutomatedBackups: list[RDSDBClusterAutomatedBackup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
