from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCreateBotReplicaRequest(BaseModel):
    botId: StrictStr
    replicaRegion: StrictStr
