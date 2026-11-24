from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubFeatureDetail(BaseModel):
    FeatureStatus: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
