from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class WAFv2UpdateManagedRuleSetVersionExpiryDateResponse(BaseModel):
    ExpiringVersion: StrictStr | None = None
    ExpiryTimestamp: datetime.datetime | StrictStr | None = None
    NextLockToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
