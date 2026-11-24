from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetTaskTemplateRequest(BaseModel):
    InstanceId: StrictStr
    TaskTemplateId: StrictStr
    SnapshotVersion: StrictStr | None = None
