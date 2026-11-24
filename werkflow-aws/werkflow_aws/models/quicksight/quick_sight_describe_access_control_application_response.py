from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_access_control_application import QuickSightAccessControlApplication


class QuickSightDescribeAccessControlApplicationResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    AccessControlApplication: QuickSightAccessControlApplication | None = None
    ResponseMetadata: dict[str, Any] | None = None
