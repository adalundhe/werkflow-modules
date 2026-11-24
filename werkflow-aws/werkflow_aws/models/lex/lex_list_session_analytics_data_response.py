from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_session_specification import LexSessionSpecification


class LexListSessionAnalyticsDataResponse(BaseModel):
    botId: StrictStr | None = None
    nextToken: StrictStr | None = None
    sessions: list[LexSessionSpecification] | None = None
    ResponseMetadata: dict[str, Any] | None = None
