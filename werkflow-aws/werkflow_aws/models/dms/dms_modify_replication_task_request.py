from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSModifyReplicationTaskRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    ReplicationTaskIdentifier: StrictStr | None = None
    MigrationType: Literal['full-load', 'cdc', 'full-load-and-cdc'] | None = None
    TableMappings: StrictStr | None = None
    ReplicationTaskSettings: StrictStr | None = None
    CdcStartTime: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
    TaskData: StrictStr | None = None
