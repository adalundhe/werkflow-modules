from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateClusterSchedulerConfigResponse(BaseModel):
    ClusterSchedulerConfigArn: StrictStr | None = None
    ClusterSchedulerConfigId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
