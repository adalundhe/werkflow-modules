from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteBotReplicaResponse(BaseModel):
    botId: StrictStr | None = None
    replicaRegion: StrictStr | None = None
    botReplicaStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
