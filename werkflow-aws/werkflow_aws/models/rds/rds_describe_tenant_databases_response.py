from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_tenant_database import RDSTenantDatabase


class RDSDescribeTenantDatabasesResponse(BaseModel):
    Marker: StrictStr | None = None
    TenantDatabases: list[RDSTenantDatabase] | None = None
    ResponseMetadata: dict[str, Any] | None = None
