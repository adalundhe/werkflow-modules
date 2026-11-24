from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_tenant_database import RDSTenantDatabase


class RDSDeleteTenantDatabaseResponse(BaseModel):
    TenantDatabase: RDSTenantDatabase | None = None
    ResponseMetadata: dict[str, Any] | None = None
