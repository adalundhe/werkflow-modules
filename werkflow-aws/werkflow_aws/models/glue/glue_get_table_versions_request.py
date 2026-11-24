from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_audit_context import GlueAuditContext


class GlueGetTableVersionsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    AuditContext: GlueAuditContext | None = None
