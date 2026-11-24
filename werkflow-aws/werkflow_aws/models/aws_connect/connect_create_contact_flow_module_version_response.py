from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateContactFlowModuleVersionResponse(BaseModel):
    ContactFlowModuleArn: StrictStr | None = None
    Version: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
