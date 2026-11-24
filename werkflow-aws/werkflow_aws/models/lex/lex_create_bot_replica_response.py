from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexCreateBotReplicaResponse(BaseModel):
    botId: StrictStr | None = None
    replicaRegion: StrictStr | None = None
    sourceRegion: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    botReplicaStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
