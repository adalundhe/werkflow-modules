from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotAnalyzerHistorySummary(BaseModel):
    botAnalyzerStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    botAnalyzerRequestId: StrictStr | None = None
