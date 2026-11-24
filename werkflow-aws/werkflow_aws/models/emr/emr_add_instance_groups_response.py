from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EMRAddInstanceGroupsResponse(BaseModel):
    JobFlowId: StrictStr | None = None
    InstanceGroupIds: list[StrictStr] | None = None
    ClusterArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
