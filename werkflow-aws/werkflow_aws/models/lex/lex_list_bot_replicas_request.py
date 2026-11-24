from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexListBotReplicasRequest(BaseModel):
    botId: StrictStr
