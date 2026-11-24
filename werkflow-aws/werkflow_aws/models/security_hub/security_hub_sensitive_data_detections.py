from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_occurrences import SecurityHubOccurrences


class SecurityHubSensitiveDataDetections(BaseModel):
    Count: StrictInt | None = None
    Type: StrictStr | None = None
    Occurrences: SecurityHubOccurrences | None = None
