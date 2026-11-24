from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowPardotConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
    isSandboxEnvironment: StrictBool | None = None
    businessUnitId: StrictStr | None = None
