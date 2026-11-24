from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowVeevaConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
