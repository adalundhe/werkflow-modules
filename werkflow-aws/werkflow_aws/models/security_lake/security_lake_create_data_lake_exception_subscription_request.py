from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityLakeCreateDataLakeExceptionSubscriptionRequest(BaseModel):
    notificationEndpoint: StrictStr
    subscriptionProtocol: StrictStr
    exceptionTimeToLive: StrictInt | None = None
