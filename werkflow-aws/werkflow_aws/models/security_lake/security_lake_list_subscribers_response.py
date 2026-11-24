from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_lake_subscriber_resource import SecurityLakeSubscriberResource


class SecurityLakeListSubscribersResponse(BaseModel):
    nextToken: StrictStr | None = None
    subscribers: list[SecurityLakeSubscriberResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
