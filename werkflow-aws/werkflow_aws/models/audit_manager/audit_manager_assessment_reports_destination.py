from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerAssessmentReportsDestination(BaseModel):
    destinationType: StrictStr | None = None
    destination: StrictStr | None = None
