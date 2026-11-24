from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStartOnDemandAuditTaskRequest(BaseModel):
    targetCheckNames: list[StrictStr]
