from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightUpdateBrandPublishedVersionResponse(BaseModel):
    RequestId: StrictStr | None = None
    VersionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
