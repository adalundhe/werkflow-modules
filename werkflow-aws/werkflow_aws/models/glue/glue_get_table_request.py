from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_audit_context import GlueAuditContext


class GlueGetTableRequest(BaseModel):
    DatabaseName: StrictStr
    Name: StrictStr
    CatalogId: StrictStr | None = None
    TransactionId: StrictStr | None = None
    QueryAsOfTime: datetime.datetime | StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    IncludeStatusDetails: StrictBool | None = None
    AttributesToGet: list[Literal['NAME', 'TABLE_TYPE', 'DEFAULT', 'LATEST_ICEBERG_METADATA']] | None = None
