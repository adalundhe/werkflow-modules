from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_generation_summary import LexGenerationSummary


class LexListBotResourceGenerationsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    generationSummaries: list[LexGenerationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
