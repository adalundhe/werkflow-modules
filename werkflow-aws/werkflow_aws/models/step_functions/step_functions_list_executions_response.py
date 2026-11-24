from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_execution_list_item import StepFunctionsExecutionListItem


class StepFunctionsListExecutionsResponse(BaseModel):
    executions: list[StepFunctionsExecutionListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
