from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_access_control_application_summary import QuickSightAccessControlApplicationSummary


class QuickSightListAccessControlApplicationsResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    AccessControlApplications: list[QuickSightAccessControlApplicationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
