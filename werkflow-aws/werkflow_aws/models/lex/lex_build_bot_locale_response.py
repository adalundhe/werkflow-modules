from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexBuildBotLocaleResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botLocaleStatus: StrictStr | None = None
    lastBuildSubmittedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
