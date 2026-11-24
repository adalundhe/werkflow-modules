from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMoveClusterNodesError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    NodeId: StrictStr | None = None
