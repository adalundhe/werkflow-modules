from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubFreeTrialStatus(BaseModel):
    FeatureType: StrictStr | None = None
    Status: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
