from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateContactFlowResponse(BaseModel):
    ContactFlowId: StrictStr | None = None
    ContactFlowArn: StrictStr | None = None
    FlowContentSha256: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
