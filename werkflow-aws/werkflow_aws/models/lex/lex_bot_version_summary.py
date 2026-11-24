from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotVersionSummary(BaseModel):
    botName: StrictStr | None = None
    botVersion: StrictStr | None = None
    description: StrictStr | None = None
    botStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
