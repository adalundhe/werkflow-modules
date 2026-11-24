from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_solution_update_config import PersonalizeSolutionUpdateConfig


class PersonalizeUpdateSolutionRequest(BaseModel):
    solutionArn: StrictStr
    performAutoTraining: StrictBool | None = None
    performIncrementalUpdate: StrictBool | None = None
    solutionUpdateConfig: PersonalizeSolutionUpdateConfig | None = None
