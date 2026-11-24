from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_replica_summary import LexBotReplicaSummary


class LexListBotReplicasResponse(BaseModel):
    botId: StrictStr | None = None
    sourceRegion: StrictStr | None = None
    botReplicaSummaries: list[LexBotReplicaSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
