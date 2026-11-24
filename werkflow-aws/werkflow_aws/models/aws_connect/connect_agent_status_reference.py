from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectAgentStatusReference(BaseModel):
    StatusStartTimestamp: datetime.datetime | StrictStr | None = None
    StatusArn: StrictStr | None = None
    StatusName: StrictStr | None = None
