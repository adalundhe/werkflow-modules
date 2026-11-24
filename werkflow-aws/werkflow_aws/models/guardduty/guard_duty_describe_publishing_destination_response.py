from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_destination_properties import GuardDutyDestinationProperties


class GuardDutyDescribePublishingDestinationResponse(BaseModel):
    DestinationId: StrictStr | None = None
    DestinationType: StrictStr | None = None
    Status: StrictStr | None = None
    PublishingFailureStartTimestamp: StrictInt | None = None
    DestinationProperties: GuardDutyDestinationProperties | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
