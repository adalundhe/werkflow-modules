from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDescribeBotReplicaResponse(BaseModel):
    botId: StrictStr | None = None
    replicaRegion: StrictStr | None = None
    sourceRegion: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    botReplicaStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
