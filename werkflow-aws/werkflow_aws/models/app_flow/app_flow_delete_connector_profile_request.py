from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowDeleteConnectorProfileRequest(BaseModel):
    connectorProfileName: StrictStr
    forceDelete: StrictBool | None = None
