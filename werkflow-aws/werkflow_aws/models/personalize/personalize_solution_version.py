from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .personalize_solution_config import PersonalizeSolutionConfig
from .personalize_tuned_hpo_params import PersonalizeTunedHPOParams


class PersonalizeSolutionVersion(BaseModel):
    name: StrictStr | None = None
    solutionVersionArn: StrictStr | None = None
    solutionArn: StrictStr | None = None
    performHPO: StrictBool | None = None
    performAutoML: StrictBool | None = None
    performIncrementalUpdate: StrictBool | None = None
    recipeArn: StrictStr | None = None
    eventType: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    solutionConfig: PersonalizeSolutionConfig | None = None
    trainingHours: StrictFloat | StrictInt | None = None
    trainingMode: StrictStr | None = None
    tunedHPOParams: PersonalizeTunedHPOParams | None = None
    status: StrictStr | None = None
    failureReason: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    trainingType: StrictStr | None = None
