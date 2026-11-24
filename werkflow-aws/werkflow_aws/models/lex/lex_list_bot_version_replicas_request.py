from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_version_replica_sort_by import LexBotVersionReplicaSortBy


class LexListBotVersionReplicasRequest(BaseModel):
    botId: StrictStr
    replicaRegion: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: LexBotVersionReplicaSortBy | None = None
