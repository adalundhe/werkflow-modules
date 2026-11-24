from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactFlowModuleContentRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    Content: StrictStr | None = None
    Settings: StrictStr | None = None
