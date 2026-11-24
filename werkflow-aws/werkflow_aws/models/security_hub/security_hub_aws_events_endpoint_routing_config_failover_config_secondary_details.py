from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails(BaseModel):
    Route: StrictStr | None = None
