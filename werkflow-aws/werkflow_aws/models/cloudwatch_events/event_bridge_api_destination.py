from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeApiDestination(BaseModel):
    ApiDestinationArn: StrictStr | None = None
    Name: StrictStr | None = None
    ApiDestinationState: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    InvocationEndpoint: StrictStr | None = None
    HttpMethod: StrictStr | None = None
    InvocationRateLimitPerSecond: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
