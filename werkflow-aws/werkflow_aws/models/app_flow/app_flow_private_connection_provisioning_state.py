from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowPrivateConnectionProvisioningState(BaseModel):
    status: StrictStr | None = None
    failureMessage: StrictStr | None = None
    failureCause: StrictStr | None = None
