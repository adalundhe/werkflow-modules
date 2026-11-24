from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchDeleteClusterNodesError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    NodeId: StrictStr | None = None
