from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_history_event_execution_data_details import StepFunctionsHistoryEventExecutionDataDetails


class StepFunctionsStateEnteredEventDetails(BaseModel):
    name: StrictStr | None = None
    input: StrictStr | None = None
    inputDetails: StepFunctionsHistoryEventExecutionDataDetails | None = None
