from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerAWSService(BaseModel):
    serviceName: StrictStr | None = None
