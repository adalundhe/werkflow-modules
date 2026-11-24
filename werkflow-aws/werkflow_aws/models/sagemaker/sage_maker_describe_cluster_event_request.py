from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeClusterEventRequest(BaseModel):
    EventId: StrictStr
    ClusterName: StrictStr
