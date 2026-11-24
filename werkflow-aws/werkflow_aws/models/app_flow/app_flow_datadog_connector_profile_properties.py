from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDatadogConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
