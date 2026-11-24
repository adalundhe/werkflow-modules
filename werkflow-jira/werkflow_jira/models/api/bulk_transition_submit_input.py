from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BulkTransitionSubmitInput(BaseModel):
    selectedIssueIdsOrKeys: list[StrictStr] | None = None
    transitionId: StrictStr | None = None
