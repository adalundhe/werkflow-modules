from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSServiceEvent(BaseModel):
    id: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
