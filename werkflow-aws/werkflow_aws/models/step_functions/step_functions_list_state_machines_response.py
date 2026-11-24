from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_state_machine_list_item import StepFunctionsStateMachineListItem


class StepFunctionsListStateMachinesResponse(BaseModel):
    stateMachines: list[StepFunctionsStateMachineListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
