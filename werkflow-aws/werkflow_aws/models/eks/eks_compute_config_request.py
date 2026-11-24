from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSComputeConfigRequest(BaseModel):
    enabled: StrictBool | None = None
    nodePools: list[StrictStr] | None = None
    nodeRoleArn: StrictStr | None = None
