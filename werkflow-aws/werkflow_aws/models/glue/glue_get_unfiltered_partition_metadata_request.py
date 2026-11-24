from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_audit_context import GlueAuditContext
from .glue_query_session_context import GlueQuerySessionContext


class GlueGetUnfilteredPartitionMetadataRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    SupportedPermissionTypes: list[Literal['COLUMN_PERMISSION', 'CELL_FILTER_PERMISSION', 'NESTED_PERMISSION', 'NESTED_CELL_PERMISSION']]
    Region: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    QuerySessionContext: GlueQuerySessionContext | None = None
