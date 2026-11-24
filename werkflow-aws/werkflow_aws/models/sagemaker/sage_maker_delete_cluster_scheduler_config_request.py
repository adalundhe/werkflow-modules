from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteClusterSchedulerConfigRequest(BaseModel):
    ClusterSchedulerConfigId: StrictStr
