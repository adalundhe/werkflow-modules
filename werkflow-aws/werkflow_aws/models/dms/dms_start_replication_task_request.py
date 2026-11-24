from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSStartReplicationTaskRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    StartReplicationTaskType: Literal['start-replication', 'resume-processing', 'reload-target']
    CdcStartTime: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
