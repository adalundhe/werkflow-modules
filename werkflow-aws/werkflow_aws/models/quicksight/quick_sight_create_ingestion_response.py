from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateIngestionResponse(BaseModel):
    Arn: StrictStr | None = None
    IngestionId: StrictStr | None = None
    IngestionStatus: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
