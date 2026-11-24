from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDynatraceConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
