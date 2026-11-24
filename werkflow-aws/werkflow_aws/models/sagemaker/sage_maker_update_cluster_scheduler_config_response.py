from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUpdateClusterSchedulerConfigResponse(BaseModel):
    ClusterSchedulerConfigArn: StrictStr | None = None
    ClusterSchedulerConfigVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
