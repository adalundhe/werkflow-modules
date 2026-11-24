from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_rollback_config import EKSRollbackConfig


class EKSUpdateClusterVersionRequest(BaseModel):
    name: StrictStr
    version: StrictStr
    clientRequestToken: StrictStr | None = None
    force: StrictBool | None = None
    rollbackConfig: EKSRollbackConfig | None = None
