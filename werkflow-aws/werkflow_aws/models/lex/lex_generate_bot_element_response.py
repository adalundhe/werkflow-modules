from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_sample_utterance import LexSampleUtterance


class LexGenerateBotElementResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    intentId: StrictStr | None = None
    sampleUtterances: list[LexSampleUtterance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
