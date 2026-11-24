from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeEventSourceResponse(BaseModel):
    Arn: StrictStr | None = None
    CreatedBy: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
