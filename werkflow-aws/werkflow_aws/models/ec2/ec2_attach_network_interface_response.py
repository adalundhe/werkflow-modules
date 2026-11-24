from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EC2AttachNetworkInterfaceResponse(BaseModel):
    AttachmentId: StrictStr | None = None
    NetworkCardIndex: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
