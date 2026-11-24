from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .step_functions_tag import StepFunctionsTag


class StepFunctionsListTagsForResourceResponse(BaseModel):
    tags: list[StepFunctionsTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
