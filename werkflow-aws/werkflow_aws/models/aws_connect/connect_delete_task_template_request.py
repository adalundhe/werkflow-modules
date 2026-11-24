from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteTaskTemplateRequest(BaseModel):
    InstanceId: StrictStr
    TaskTemplateId: StrictStr
