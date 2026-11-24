from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerAWSAccount(BaseModel):
    id: StrictStr | None = None
    emailAddress: StrictStr | None = None
    name: StrictStr | None = None
