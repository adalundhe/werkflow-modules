from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateContactFlowModuleVersionRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    Description: StrictStr | None = None
    FlowModuleContentSha256: StrictStr | None = None
