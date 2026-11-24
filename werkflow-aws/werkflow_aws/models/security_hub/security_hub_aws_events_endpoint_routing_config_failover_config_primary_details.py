from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails(BaseModel):
    HealthCheck: StrictStr | None = None
