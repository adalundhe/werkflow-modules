from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_audit_context import GlueAuditContext


class GlueGetTableVersionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    VersionId: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
