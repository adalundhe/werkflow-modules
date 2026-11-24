from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_version_locale_details import LexBotVersionLocaleDetails


class LexCreateBotVersionResponse(BaseModel):
    botId: StrictStr | None = None
    description: StrictStr | None = None
    botVersion: StrictStr | None = None
    botVersionLocaleSpecification: dict[StrictStr, LexBotVersionLocaleDetails] | None = None
    botStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
