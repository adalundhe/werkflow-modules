from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_lex_bot import ConnectLexBot
from .connect_lex_v2_bot import ConnectLexV2Bot


class ConnectDisassociateBotRequest(BaseModel):
    InstanceId: StrictStr
    LexBot: ConnectLexBot | None = None
    LexV2Bot: ConnectLexV2Bot | None = None
    ClientToken: StrictStr | None = None
