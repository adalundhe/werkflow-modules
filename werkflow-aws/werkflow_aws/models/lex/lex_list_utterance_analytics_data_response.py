from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_utterance_specification import LexUtteranceSpecification


class LexListUtteranceAnalyticsDataResponse(BaseModel):
    botId: StrictStr | None = None
    nextToken: StrictStr | None = None
    utterances: list[LexUtteranceSpecification] | None = None
    ResponseMetadata: dict[str, Any] | None = None
