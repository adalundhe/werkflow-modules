from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_history_event_execution_data_details import StepFunctionsHistoryEventExecutionDataDetails


class StepFunctionsTaskSubmittedEventDetails(BaseModel):
    resourceType: StrictStr | None = None
    resource: StrictStr | None = None
    output: StrictStr | None = None
    outputDetails: StepFunctionsHistoryEventExecutionDataDetails | None = None
