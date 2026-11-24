from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_instance_automated_backup import RDSDBInstanceAutomatedBackup


class RDSDescribeDBInstanceAutomatedBackupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBInstanceAutomatedBackups: list[RDSDBInstanceAutomatedBackup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
