from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowZendeskConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
