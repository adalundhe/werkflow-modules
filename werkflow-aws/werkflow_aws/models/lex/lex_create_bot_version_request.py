from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_bot_version_locale_details import LexBotVersionLocaleDetails


class LexCreateBotVersionRequest(BaseModel):
    botId: StrictStr
    botVersionLocaleSpecification: dict[StrictStr, LexBotVersionLocaleDetails]
    description: StrictStr | None = None
