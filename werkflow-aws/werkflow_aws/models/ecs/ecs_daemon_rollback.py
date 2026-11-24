from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSDaemonRollback(BaseModel):
    reason: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    rollbackTargetDaemonRevisionArn: StrictStr | None = None
    rollbackCapacityProviders: list[StrictStr] | None = None
