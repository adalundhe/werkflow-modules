from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_log_subscription import DirectoryServiceLogSubscription


class DirectoryServiceListLogSubscriptionsResponse(BaseModel):
    LogSubscriptions: list[DirectoryServiceLogSubscription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
