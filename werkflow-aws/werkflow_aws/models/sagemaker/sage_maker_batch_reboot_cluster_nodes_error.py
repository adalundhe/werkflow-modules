from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchRebootClusterNodesError(BaseModel):
    NodeId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
