from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_auto_ml_result import PersonalizeAutoMLResult
from .personalize_solution_config import PersonalizeSolutionConfig
from .personalize_solution_update_summary import PersonalizeSolutionUpdateSummary
from .personalize_solution_version_summary import PersonalizeSolutionVersionSummary


class PersonalizeSolution(BaseModel):
    name: StrictStr | None = None
    solutionArn: StrictStr | None = None
    performHPO: StrictBool | None = None
    performAutoML: StrictBool | None = None
    performAutoTraining: StrictBool | None = None
    performIncrementalUpdate: StrictBool | None = None
    recipeArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    eventType: StrictStr | None = None
    solutionConfig: PersonalizeSolutionConfig | None = None
    autoMLResult: PersonalizeAutoMLResult | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    latestSolutionVersion: PersonalizeSolutionVersionSummary | None = None
    latestSolutionUpdate: PersonalizeSolutionUpdateSummary | None = None
