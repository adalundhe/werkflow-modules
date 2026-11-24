from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotAliasReplicaSummary(BaseModel):
    botAliasId: StrictStr | None = None
    botAliasReplicationStatus: StrictStr | None = None
    botVersion: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
