from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MediaStoreGetLifecyclePolicyResponse(BaseModel):
    LifecyclePolicy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
