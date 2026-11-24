from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruListNotificationChannelsRequest(BaseModel):
    NextToken: StrictStr | None = None
