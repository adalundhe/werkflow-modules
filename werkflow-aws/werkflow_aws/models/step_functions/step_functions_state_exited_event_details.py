from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_assigned_variables_details import StepFunctionsAssignedVariablesDetails
from .step_functions_history_event_execution_data_details import StepFunctionsHistoryEventExecutionDataDetails


class StepFunctionsStateExitedEventDetails(BaseModel):
    name: StrictStr | None = None
    output: StrictStr | None = None
    outputDetails: StepFunctionsHistoryEventExecutionDataDetails | None = None
    assignedVariables: dict[StrictStr, StrictStr] | None = None
    assignedVariablesDetails: StepFunctionsAssignedVariablesDetails | None = None
