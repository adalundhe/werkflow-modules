from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateContactFlowVersionResponse(BaseModel):
    ContactFlowArn: StrictStr | None = None
    Version: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
