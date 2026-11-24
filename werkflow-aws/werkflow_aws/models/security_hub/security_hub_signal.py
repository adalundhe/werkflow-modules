from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_indicator import SecurityHubIndicator


class SecurityHubSignal(BaseModel):
    Type: StrictStr | None = None
    Id: StrictStr | None = None
    Title: StrictStr | None = None
    ProductArn: StrictStr | None = None
    ResourceIds: list[StrictStr] | None = None
    SignalIndicators: list[SecurityHubIndicator] | None = None
    Name: StrictStr | None = None
    CreatedAt: StrictInt | None = None
    UpdatedAt: StrictInt | None = None
    FirstSeenAt: StrictInt | None = None
    LastSeenAt: StrictInt | None = None
    Severity: StrictFloat | StrictInt | None = None
    Count: StrictInt | None = None
    ActorIds: list[StrictStr] | None = None
    EndpointIds: list[StrictStr] | None = None
