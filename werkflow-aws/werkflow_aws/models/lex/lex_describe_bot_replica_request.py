from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotReplicaRequest(BaseModel):
    botId: StrictStr
    replicaRegion: StrictStr
