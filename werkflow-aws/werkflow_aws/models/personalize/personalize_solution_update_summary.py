from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_solution_update_config import PersonalizeSolutionUpdateConfig


class PersonalizeSolutionUpdateSummary(BaseModel):
    solutionUpdateConfig: PersonalizeSolutionUpdateConfig | None = None
    status: StrictStr | None = None
    performAutoTraining: StrictBool | None = None
    performIncrementalUpdate: StrictBool | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
