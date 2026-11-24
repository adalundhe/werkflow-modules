from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAttendee(BaseModel):
    AttendeeId: StrictStr | None = None
    JoinToken: StrictStr | None = None
