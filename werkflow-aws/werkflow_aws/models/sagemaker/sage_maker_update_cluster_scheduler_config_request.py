from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_scheduler_config import SageMakerSchedulerConfig


class SageMakerUpdateClusterSchedulerConfigRequest(BaseModel):
    ClusterSchedulerConfigId: StrictStr
    TargetVersion: StrictInt
    SchedulerConfig: SageMakerSchedulerConfig | None = None
    Description: StrictStr | None = None
