from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQUserPendingChanges(BaseModel):
    ConsoleAccess: StrictBool | None = None
    Groups: list[StrictStr] | None = None
    PendingChange: StrictStr | None = None
