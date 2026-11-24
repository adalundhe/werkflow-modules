from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchStartDomainMaintenanceRequest(BaseModel):
    DomainName: StrictStr
    Action: Literal['REBOOT_NODE', 'RESTART_SEARCH_PROCESS', 'RESTART_DASHBOARD']
    NodeId: StrictStr | None = None
