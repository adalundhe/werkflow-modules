from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeClusterOperationRequest(BaseModel):
    ClusterName: StrictStr
    OperationId: StrictStr
