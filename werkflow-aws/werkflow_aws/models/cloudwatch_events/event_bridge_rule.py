from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeRule(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    EventPattern: StrictStr | None = None
    State: StrictStr | None = None
    Description: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ManagedBy: StrictStr | None = None
    EventBusName: StrictStr | None = None
