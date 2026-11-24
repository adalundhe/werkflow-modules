from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightGetDashboardEmbedUrlResponse(BaseModel):
    EmbedUrl: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
