from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchListDomainMaintenancesRequest(BaseModel):
    DomainName: StrictStr
    Action: Literal['REBOOT_NODE', 'RESTART_SEARCH_PROCESS', 'RESTART_DASHBOARD'] | None = None
    Status: Literal['PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'TIMED_OUT'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
