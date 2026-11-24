from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppFlowRegisterConnectorResponse(BaseModel):
    connectorArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
