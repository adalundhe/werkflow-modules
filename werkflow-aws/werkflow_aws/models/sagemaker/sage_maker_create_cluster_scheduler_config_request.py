from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_scheduler_config import SageMakerSchedulerConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateClusterSchedulerConfigRequest(BaseModel):
    Name: StrictStr
    ClusterArn: StrictStr
    SchedulerConfig: SageMakerSchedulerConfig
    Description: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
