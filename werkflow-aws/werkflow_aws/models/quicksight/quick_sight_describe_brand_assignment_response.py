from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightDescribeBrandAssignmentResponse(BaseModel):
    RequestId: StrictStr | None = None
    BrandArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
