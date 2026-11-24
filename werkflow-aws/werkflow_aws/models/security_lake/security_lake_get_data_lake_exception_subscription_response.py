from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityLakeGetDataLakeExceptionSubscriptionResponse(BaseModel):
    exceptionTimeToLive: StrictInt | None = None
    notificationEndpoint: StrictStr | None = None
    subscriptionProtocol: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
