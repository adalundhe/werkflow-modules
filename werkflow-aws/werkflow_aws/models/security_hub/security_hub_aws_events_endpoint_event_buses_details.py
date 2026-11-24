from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventsEndpointEventBusesDetails(BaseModel):
    EventBusArn: StrictStr | None = None
