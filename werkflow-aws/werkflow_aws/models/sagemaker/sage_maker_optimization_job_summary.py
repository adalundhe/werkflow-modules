from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerOptimizationJobSummary(BaseModel):
    OptimizationJobName: StrictStr | None = None
    OptimizationJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    OptimizationJobStatus: StrictStr | None = None
    OptimizationStartTime: datetime.datetime | StrictStr | None = None
    OptimizationEndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DeploymentInstanceType: StrictStr | None = None
    MaxInstanceCount: StrictInt | None = None
    OptimizationTypes: list[StrictStr] | None = None
