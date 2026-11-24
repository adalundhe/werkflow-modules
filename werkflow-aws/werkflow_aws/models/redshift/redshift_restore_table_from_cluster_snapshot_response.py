from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_table_restore_status import RedshiftTableRestoreStatus


class RedshiftRestoreTableFromClusterSnapshotResponse(BaseModel):
    TableRestoreStatus: RedshiftTableRestoreStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
