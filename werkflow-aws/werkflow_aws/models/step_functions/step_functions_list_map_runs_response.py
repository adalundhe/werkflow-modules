from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_map_run_list_item import StepFunctionsMapRunListItem


class StepFunctionsListMapRunsResponse(BaseModel):
    mapRuns: list[StepFunctionsMapRunListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
