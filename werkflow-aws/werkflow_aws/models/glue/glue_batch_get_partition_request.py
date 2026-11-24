from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_audit_context import GlueAuditContext
from .glue_partition_value_list import GluePartitionValueList
from .glue_query_session_context import GlueQuerySessionContext


class GlueBatchGetPartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionsToGet: list[GluePartitionValueList]
    CatalogId: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    QuerySessionContext: GlueQuerySessionContext | None = None
