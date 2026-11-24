from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetOrganizationsAccessReportRequest(BaseModel):
    JobId: StrictStr
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
    SortKey: Literal['SERVICE_NAMESPACE_ASCENDING', 'SERVICE_NAMESPACE_DESCENDING', 'LAST_AUTHENTICATED_TIME_ASCENDING', 'LAST_AUTHENTICATED_TIME_DESCENDING'] | None = None
