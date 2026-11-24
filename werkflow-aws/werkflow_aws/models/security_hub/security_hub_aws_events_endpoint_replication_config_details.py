from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventsEndpointReplicationConfigDetails(BaseModel):
    State: StrictStr | None = None
