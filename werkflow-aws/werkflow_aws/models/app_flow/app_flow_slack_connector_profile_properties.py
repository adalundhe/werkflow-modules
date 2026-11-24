from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSlackConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
