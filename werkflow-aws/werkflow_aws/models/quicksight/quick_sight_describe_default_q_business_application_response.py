from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeDefaultQBusinessApplicationResponse(BaseModel):
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ApplicationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
