from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKAssessmentParameters(BaseModel):
    TargetInstanceType: StrictStr | None = None
