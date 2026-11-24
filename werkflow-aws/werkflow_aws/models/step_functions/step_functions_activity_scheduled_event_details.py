from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .step_functions_history_event_execution_data_details import StepFunctionsHistoryEventExecutionDataDetails


class StepFunctionsActivityScheduledEventDetails(BaseModel):
    resource: StrictStr | None = None
    input: StrictStr | None = None
    inputDetails: StepFunctionsHistoryEventExecutionDataDetails | None = None
    timeoutInSeconds: StrictInt | None = None
    heartbeatInSeconds: StrictInt | None = None
