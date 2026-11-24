from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupControlScope(BaseModel):
    ComplianceResourceIds: list[StrictStr] | None = None
    ComplianceResourceTypes: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
