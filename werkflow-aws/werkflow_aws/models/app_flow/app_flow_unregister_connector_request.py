from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowUnregisterConnectorRequest(BaseModel):
    connectorLabel: StrictStr
    forceDelete: StrictBool | None = None
