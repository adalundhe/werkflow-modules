from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetDomainMaintenanceStatusRequest(BaseModel):
    DomainName: StrictStr
    MaintenanceId: StrictStr
