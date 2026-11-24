from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowMarketoConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
