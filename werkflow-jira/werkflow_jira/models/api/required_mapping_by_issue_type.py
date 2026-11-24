from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RequiredMappingByIssueType(BaseModel):
    issueTypeId: StrictStr | None = None
    statusIds: list[StrictStr] | None = None
