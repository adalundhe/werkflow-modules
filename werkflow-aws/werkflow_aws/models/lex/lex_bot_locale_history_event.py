from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotLocaleHistoryEvent(BaseModel):
    event: StrictStr | None = None
    eventDate: datetime.datetime | StrictStr | None = None
