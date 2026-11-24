from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_solution_config import PersonalizeSolutionConfig
from .personalize_tag import PersonalizeTag


class PersonalizeCreateSolutionRequest(BaseModel):
    name: StrictStr
    datasetGroupArn: StrictStr
    performHPO: StrictBool | None = None
    performAutoML: StrictBool | None = None
    performAutoTraining: StrictBool | None = None
    performIncrementalUpdate: StrictBool | None = None
    recipeArn: StrictStr | None = None
    eventType: StrictStr | None = None
    solutionConfig: PersonalizeSolutionConfig | None = None
    tags: list[PersonalizeTag] | None = None
