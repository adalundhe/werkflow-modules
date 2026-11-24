from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAccountStatus(BaseModel):
    AccountId: StrictStr | None = None
    SLRDeploymentStatus: StrictStr | None = None
