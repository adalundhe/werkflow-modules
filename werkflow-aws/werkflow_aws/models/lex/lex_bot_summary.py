from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotSummary(BaseModel):
    botId: StrictStr | None = None
    botName: StrictStr | None = None
    description: StrictStr | None = None
    botStatus: StrictStr | None = None
    latestBotVersion: StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    botType: StrictStr | None = None
