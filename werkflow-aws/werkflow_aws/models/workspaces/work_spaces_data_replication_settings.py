from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesDataReplicationSettings(BaseModel):
    DataReplication: StrictStr | None = None
    RecoverySnapshotTime: datetime.datetime | StrictStr | None = None
