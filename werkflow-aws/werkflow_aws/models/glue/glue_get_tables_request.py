from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_audit_context import GlueAuditContext


class GlueGetTablesRequest(BaseModel):
    DatabaseName: StrictStr
    CatalogId: StrictStr | None = None
    Expression: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    TransactionId: StrictStr | None = None
    QueryAsOfTime: datetime.datetime | StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    ResourceShareType: Literal['FEDERATED', 'ALL'] | None = None
    IncludeStatusDetails: StrictBool | None = None
    AttributesToGet: list[Literal['NAME', 'TABLE_TYPE', 'DEFAULT', 'LATEST_ICEBERG_METADATA']] | None = None
