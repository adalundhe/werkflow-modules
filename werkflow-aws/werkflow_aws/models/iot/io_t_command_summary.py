from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCommandSummary(BaseModel):
    commandArn: StrictStr | None = None
    commandId: StrictStr | None = None
    displayName: StrictStr | None = None
    deprecated: StrictBool | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    pendingDeletion: StrictBool | None = None
