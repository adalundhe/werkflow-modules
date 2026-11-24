from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrderOfIssueTypes(BaseModel):
    after: StrictStr | None = None
    issueTypeIds: list[StrictStr] | None = None
    position: StrictStr | None = None
