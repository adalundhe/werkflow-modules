from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_version_replica_summary import LexBotVersionReplicaSummary


class LexListBotVersionReplicasResponse(BaseModel):
    botId: StrictStr | None = None
    sourceRegion: StrictStr | None = None
    replicaRegion: StrictStr | None = None
    botVersionReplicaSummaries: list[LexBotVersionReplicaSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
