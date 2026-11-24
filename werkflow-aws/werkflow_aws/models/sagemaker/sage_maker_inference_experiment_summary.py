from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_experiment_schedule import SageMakerInferenceExperimentSchedule


class SageMakerInferenceExperimentSummary(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Schedule: SageMakerInferenceExperimentSchedule | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    RoleArn: StrictStr | None = None
