from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_calculation_summary import AthenaCalculationSummary


class AthenaListCalculationExecutionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Calculations: list[AthenaCalculationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
