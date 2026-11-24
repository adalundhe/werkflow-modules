from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CreateExclusionRulesRequest(BaseModel):
    issueIds: list[StrictInt] | None = None
    issueTypeIds: list[StrictInt] | None = None
    numberOfDaysToShowCompletedIssues: StrictInt | None = None
    releaseIds: list[StrictInt] | None = None
    workStatusCategoryIds: list[StrictInt] | None = None
    workStatusIds: list[StrictInt] | None = None
