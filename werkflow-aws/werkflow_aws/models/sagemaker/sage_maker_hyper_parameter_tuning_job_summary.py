from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_objective_status_counters import SageMakerObjectiveStatusCounters
from .sage_maker_resource_limits import SageMakerResourceLimits
from .sage_maker_training_job_status_counters import SageMakerTrainingJobStatusCounters


class SageMakerHyperParameterTuningJobSummary(BaseModel):
    HyperParameterTuningJobName: StrictStr | None = None
    HyperParameterTuningJobArn: StrictStr | None = None
    HyperParameterTuningJobStatus: StrictStr | None = None
    Strategy: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    HyperParameterTuningEndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    TrainingJobStatusCounters: SageMakerTrainingJobStatusCounters | None = None
    ObjectiveStatusCounters: SageMakerObjectiveStatusCounters | None = None
    ResourceLimits: SageMakerResourceLimits | None = None
