from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_calculation_status_model import AthenaCalculationStatusModel


class AthenaCalculationSummary(BaseModel):
    CalculationExecutionId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: AthenaCalculationStatusModel | None = None
