from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_finding_history_record import SecurityHubFindingHistoryRecord


class SecurityHubGetFindingHistoryResponse(BaseModel):
    Records: list[SecurityHubFindingHistoryRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
