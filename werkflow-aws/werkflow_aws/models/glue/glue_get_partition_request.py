from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_audit_context import GlueAuditContext


class GlueGetPartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    CatalogId: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
