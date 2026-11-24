from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowServiceNowConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
