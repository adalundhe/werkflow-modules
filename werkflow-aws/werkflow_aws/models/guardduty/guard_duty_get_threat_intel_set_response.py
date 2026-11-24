from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GuardDutyGetThreatIntelSetResponse(BaseModel):
    Name: StrictStr | None = None
    Format: StrictStr | None = None
    Location: StrictStr | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
