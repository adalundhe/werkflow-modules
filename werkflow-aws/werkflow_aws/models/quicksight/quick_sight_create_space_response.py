from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightCreateSpaceResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
