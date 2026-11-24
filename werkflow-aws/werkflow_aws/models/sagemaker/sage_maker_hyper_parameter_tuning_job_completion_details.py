from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerHyperParameterTuningJobCompletionDetails(BaseModel):
    NumberOfTrainingJobsObjectiveNotImproving: StrictInt | None = None
    ConvergenceDetectedTime: datetime.datetime | StrictStr | None = None
