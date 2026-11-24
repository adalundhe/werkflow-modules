from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectFlowModule(BaseModel):
    Type: StrictStr | None = None
    FlowModuleId: StrictStr | None = None
