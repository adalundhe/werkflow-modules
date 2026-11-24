from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowStartFlowRequest(BaseModel):
    flowName: StrictStr
    clientToken: StrictStr | None = None
