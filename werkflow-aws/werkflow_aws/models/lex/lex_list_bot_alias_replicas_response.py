from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_alias_replica_summary import LexBotAliasReplicaSummary


class LexListBotAliasReplicasResponse(BaseModel):
    botId: StrictStr | None = None
    sourceRegion: StrictStr | None = None
    replicaRegion: StrictStr | None = None
    botAliasReplicaSummaries: list[LexBotAliasReplicaSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
