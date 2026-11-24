from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class GuardDutyGetThreatEntitySetResponse(BaseModel):
    Name: StrictStr | None = None
    Format: StrictStr | None = None
    Location: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ErrorDetails: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
