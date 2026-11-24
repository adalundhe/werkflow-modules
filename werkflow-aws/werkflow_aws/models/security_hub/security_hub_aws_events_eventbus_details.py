from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventsEventbusDetails(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Policy: StrictStr | None = None
