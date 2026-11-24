from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_lex_bot import ConnectLexBot


class ConnectAssociateLexBotRequest(BaseModel):
    InstanceId: StrictStr
    LexBot: ConnectLexBot
    ClientToken: StrictStr | None = None
