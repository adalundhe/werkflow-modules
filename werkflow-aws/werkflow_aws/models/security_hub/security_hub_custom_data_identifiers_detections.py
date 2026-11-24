from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_occurrences import SecurityHubOccurrences


class SecurityHubCustomDataIdentifiersDetections(BaseModel):
    Count: StrictInt | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Occurrences: SecurityHubOccurrences | None = None
