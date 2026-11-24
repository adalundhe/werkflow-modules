from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectGetFlowAssociationResponse(BaseModel):
    ResourceId: StrictStr | None = None
    FlowId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
