from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IssueBulkDeletePayload(BaseModel):
    selectedIssueIdsOrKeys: list[StrictStr] | None = None
    sendBulkNotification: StrictBool | None = None
