from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_activity_list_item import StepFunctionsActivityListItem


class StepFunctionsListActivitiesResponse(BaseModel):
    activities: list[StepFunctionsActivityListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
