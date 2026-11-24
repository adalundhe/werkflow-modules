from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_lex_bot_config import ConnectLexBotConfig


class ConnectListBotsResponse(BaseModel):
    LexBots: list[ConnectLexBotConfig] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
