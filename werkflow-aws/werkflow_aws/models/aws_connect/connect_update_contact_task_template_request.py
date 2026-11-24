from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactTaskTemplateRequest(BaseModel):
    InstanceId: StrictStr
    TaskTemplateId: StrictStr
    ContactId: StrictStr
