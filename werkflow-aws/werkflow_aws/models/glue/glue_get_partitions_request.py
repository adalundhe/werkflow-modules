from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_audit_context import GlueAuditContext
from .glue_segment import GlueSegment


class GlueGetPartitionsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    Expression: StrictStr | None = None
    NextToken: StrictStr | None = None
    Segment: GlueSegment | None = None
    MaxResults: StrictInt | None = None
    ExcludeColumnSchema: StrictBool | None = None
    TransactionId: StrictStr | None = None
    QueryAsOfTime: datetime.datetime | StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
