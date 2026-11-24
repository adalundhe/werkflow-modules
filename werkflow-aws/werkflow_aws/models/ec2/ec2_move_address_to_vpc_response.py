from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2MoveAddressToVpcResponse(BaseModel):
    AllocationId: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
