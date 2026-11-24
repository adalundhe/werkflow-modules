from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .step_functions_mock_error_output import StepFunctionsMockErrorOutput


class StepFunctionsMockInput(BaseModel):
    result: StrictStr | None = None
    errorOutput: StepFunctionsMockErrorOutput | None = None
    fieldValidationMode: Literal['STRICT', 'PRESENT', 'NONE'] | None = None
