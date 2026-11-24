from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowInforNexusConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
