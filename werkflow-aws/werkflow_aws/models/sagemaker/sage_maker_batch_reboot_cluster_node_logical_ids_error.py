from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchRebootClusterNodeLogicalIdsError(BaseModel):
    NodeLogicalId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
