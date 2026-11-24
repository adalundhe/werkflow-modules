from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_snapshot_tenant_database import RDSDBSnapshotTenantDatabase


class RDSDescribeDBSnapshotTenantDatabasesResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSnapshotTenantDatabases: list[RDSDBSnapshotTenantDatabase] | None = None
    ResponseMetadata: dict[str, Any] | None = None
