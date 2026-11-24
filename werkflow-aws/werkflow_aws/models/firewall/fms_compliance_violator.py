from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSComplianceViolator(BaseModel):
    ResourceId: StrictStr | None = None
    ViolationReason: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
