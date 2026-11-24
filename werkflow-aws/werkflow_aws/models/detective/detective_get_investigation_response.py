from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DetectiveGetInvestigationResponse(BaseModel):
    GraphArn: StrictStr | None = None
    InvestigationId: StrictStr | None = None
    EntityArn: StrictStr | None = None
    EntityType: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ScopeStartTime: datetime.datetime | StrictStr | None = None
    ScopeEndTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Severity: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
