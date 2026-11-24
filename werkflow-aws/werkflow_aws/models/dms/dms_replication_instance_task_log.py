from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSReplicationInstanceTaskLog(BaseModel):
    ReplicationTaskName: StrictStr | None = None
    ReplicationTaskArn: StrictStr | None = None
    ReplicationInstanceTaskLogSize: StrictInt | None = None
