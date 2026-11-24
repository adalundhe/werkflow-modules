from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceCreateLogSubscriptionRequest(BaseModel):
    DirectoryId: StrictStr
    LogGroupName: StrictStr
