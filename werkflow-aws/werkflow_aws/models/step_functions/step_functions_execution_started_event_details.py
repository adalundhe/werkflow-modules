from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_history_event_execution_data_details import StepFunctionsHistoryEventExecutionDataDetails


class StepFunctionsExecutionStartedEventDetails(BaseModel):
    input: StrictStr | None = None
    inputDetails: StepFunctionsHistoryEventExecutionDataDetails | None = None
    roleArn: StrictStr | None = None
    stateMachineAliasArn: StrictStr | None = None
    stateMachineVersionArn: StrictStr | None = None
