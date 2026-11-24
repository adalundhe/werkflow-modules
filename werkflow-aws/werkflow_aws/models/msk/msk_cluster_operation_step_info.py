from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKClusterOperationStepInfo(BaseModel):
    StepStatus: StrictStr | None = None
