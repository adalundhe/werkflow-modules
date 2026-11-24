from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueAuditContext(BaseModel):
    AdditionalAuditContext: StrictStr | None = None
    RequestedColumns: list[StrictStr] | None = None
    AllColumnsRequested: StrictBool | None = None
