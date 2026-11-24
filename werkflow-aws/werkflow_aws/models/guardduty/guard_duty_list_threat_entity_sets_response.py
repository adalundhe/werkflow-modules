from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GuardDutyListThreatEntitySetsResponse(BaseModel):
    ThreatEntitySetIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
