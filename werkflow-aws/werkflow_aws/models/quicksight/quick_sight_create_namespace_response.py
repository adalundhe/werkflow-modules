from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateNamespaceResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    CapacityRegion: StrictStr | None = None
    CreationStatus: StrictStr | None = None
    IdentityStore: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
