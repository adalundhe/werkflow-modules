from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotVersionReplicaSummary(BaseModel):
    botVersion: StrictStr | None = None
    botVersionReplicationStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
