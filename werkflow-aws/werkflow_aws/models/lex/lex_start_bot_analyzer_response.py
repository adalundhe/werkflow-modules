from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexStartBotAnalyzerResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botAnalyzerStatus: StrictStr | None = None
    botAnalyzerRequestId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
