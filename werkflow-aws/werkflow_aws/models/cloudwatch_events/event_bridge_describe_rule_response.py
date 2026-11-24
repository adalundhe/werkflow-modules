from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeRuleResponse(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    EventPattern: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    State: StrictStr | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ManagedBy: StrictStr | None = None
    EventBusName: StrictStr | None = None
    CreatedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
