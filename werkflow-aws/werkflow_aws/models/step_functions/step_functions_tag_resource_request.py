from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_tag import StepFunctionsTag


class StepFunctionsTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[StepFunctionsTag]
