from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_state_machine_alias_list_item import StepFunctionsStateMachineAliasListItem


class StepFunctionsListStateMachineAliasesResponse(BaseModel):
    stateMachineAliases: list[StepFunctionsStateMachineAliasListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
