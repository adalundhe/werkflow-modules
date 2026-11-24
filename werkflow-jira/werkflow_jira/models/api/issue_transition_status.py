from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueTransitionStatus(BaseModel):
    statusId: StrictInt | None = None
    statusName: StrictStr | None = None
