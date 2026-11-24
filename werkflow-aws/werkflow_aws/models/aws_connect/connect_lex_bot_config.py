from __future__ import annotations
from pydantic import BaseModel
from .connect_lex_bot import ConnectLexBot
from .connect_lex_v2_bot import ConnectLexV2Bot


class ConnectLexBotConfig(BaseModel):
    LexBot: ConnectLexBot | None = None
    LexV2Bot: ConnectLexV2Bot | None = None
