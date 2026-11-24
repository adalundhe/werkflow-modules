from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotLocaleSummary(BaseModel):
    localeId: StrictStr | None = None
    localeName: StrictStr | None = None
    description: StrictStr | None = None
    botLocaleStatus: StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    lastBuildSubmittedDateTime: datetime.datetime | StrictStr | None = None
