from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectStateTransition(BaseModel):
    State: StrictStr | None = None
    StateStartTimestamp: datetime.datetime | StrictStr | None = None
    StateEndTimestamp: datetime.datetime | StrictStr | None = None
