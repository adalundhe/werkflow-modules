from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeleteLogSubscriptionRequest(BaseModel):
    DirectoryId: StrictStr
