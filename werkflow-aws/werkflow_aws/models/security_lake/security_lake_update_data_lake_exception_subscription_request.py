from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityLakeUpdateDataLakeExceptionSubscriptionRequest(BaseModel):
    notificationEndpoint: StrictStr
    subscriptionProtocol: StrictStr
    exceptionTimeToLive: StrictInt | None = None
