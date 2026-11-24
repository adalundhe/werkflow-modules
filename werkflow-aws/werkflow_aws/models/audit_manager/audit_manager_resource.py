from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerResource(BaseModel):
    arn: StrictStr | None = None
    value: StrictStr | None = None
    complianceCheck: StrictStr | None = None
