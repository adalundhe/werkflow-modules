from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .step_functions_log_destination import StepFunctionsLogDestination


class StepFunctionsLoggingConfiguration(BaseModel):
    level: StrictStr | None = None
    includeExecutionData: StrictBool | None = None
    destinations: list[StepFunctionsLogDestination] | None = None
