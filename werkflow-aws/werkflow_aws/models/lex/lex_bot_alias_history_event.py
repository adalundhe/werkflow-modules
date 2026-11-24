from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotAliasHistoryEvent(BaseModel):
    botVersion: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    endDate: datetime.datetime | StrictStr | None = None
