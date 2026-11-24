from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeClusterSchedulerConfigRequest(BaseModel):
    ClusterSchedulerConfigId: StrictStr
    ClusterSchedulerConfigVersion: StrictInt | None = None
