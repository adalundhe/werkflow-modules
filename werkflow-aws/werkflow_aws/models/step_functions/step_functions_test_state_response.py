from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_inspection_data import StepFunctionsInspectionData


class StepFunctionsTestStateResponse(BaseModel):
    output: StrictStr | None = None
    error: StrictStr | None = None
    cause: StrictStr | None = None
    inspectionData: StepFunctionsInspectionData | None = None
    nextState: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
