from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsServicePlacementStrategiesDetails(BaseModel):
    Field: StrictStr | None = None
    Type: StrictStr | None = None
