from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ReorderIssueResolutionsRequest(BaseModel):
    after: StrictStr | None = None
    ids: list[StrictStr] | None = None
    position: StrictStr | None = None
