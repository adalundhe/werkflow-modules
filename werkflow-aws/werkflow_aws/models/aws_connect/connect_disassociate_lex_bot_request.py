from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateLexBotRequest(BaseModel):
    InstanceId: StrictStr
    BotName: StrictStr
    LexRegion: StrictStr
    ClientToken: StrictStr | None = None
