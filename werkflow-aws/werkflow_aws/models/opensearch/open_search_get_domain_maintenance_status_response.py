from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchGetDomainMaintenanceStatusResponse(BaseModel):
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    NodeId: StrictStr | None = None
    Action: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
