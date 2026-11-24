from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_experiment_source import SageMakerExperimentSource


class SageMakerExperimentSummary(BaseModel):
    ExperimentArn: StrictStr | None = None
    ExperimentName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    ExperimentSource: SageMakerExperimentSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
