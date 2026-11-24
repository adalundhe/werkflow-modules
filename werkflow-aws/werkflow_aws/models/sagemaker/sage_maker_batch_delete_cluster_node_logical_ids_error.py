from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchDeleteClusterNodeLogicalIdsError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    NodeLogicalId: StrictStr | None = None
