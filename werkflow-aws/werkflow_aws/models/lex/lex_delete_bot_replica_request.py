from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteBotReplicaRequest(BaseModel):
    botId: StrictStr
    replicaRegion: StrictStr
