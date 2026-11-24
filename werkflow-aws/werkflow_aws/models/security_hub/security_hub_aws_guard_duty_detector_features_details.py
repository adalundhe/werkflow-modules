from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorFeaturesDetails(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
