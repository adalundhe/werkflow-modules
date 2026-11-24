from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsPutStorageTierPolicyResponse(BaseModel):
    storageTier: StrictStr | None = None
    lastUpdatedTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
