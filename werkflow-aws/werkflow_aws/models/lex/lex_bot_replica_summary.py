from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotReplicaSummary(BaseModel):
    replicaRegion: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    botReplicaStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
