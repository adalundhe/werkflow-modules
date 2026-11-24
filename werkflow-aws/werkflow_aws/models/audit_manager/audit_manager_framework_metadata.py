from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerFrameworkMetadata(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    logo: StrictStr | None = None
    complianceType: StrictStr | None = None
