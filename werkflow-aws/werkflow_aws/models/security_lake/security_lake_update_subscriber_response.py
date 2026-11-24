from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_lake_subscriber_resource import SecurityLakeSubscriberResource


class SecurityLakeUpdateSubscriberResponse(BaseModel):
    subscriber: SecurityLakeSubscriberResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
