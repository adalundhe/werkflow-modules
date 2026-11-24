from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudSearchScalingParameters(BaseModel):
    DesiredInstanceType: StrictStr | None = None
    DesiredReplicationCount: StrictInt | None = None
    DesiredPartitionCount: StrictInt | None = None
