from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_audit_context import GlueAuditContext
from .glue_query_session_context import GlueQuerySessionContext
from .glue_segment import GlueSegment


class GlueGetUnfilteredPartitionsMetadataRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    SupportedPermissionTypes: list[Literal['COLUMN_PERMISSION', 'CELL_FILTER_PERMISSION', 'NESTED_PERMISSION', 'NESTED_CELL_PERMISSION']]
    Region: StrictStr | None = None
    Expression: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    NextToken: StrictStr | None = None
    Segment: GlueSegment | None = None
    MaxResults: StrictInt | None = None
    QuerySessionContext: GlueQuerySessionContext | None = None
