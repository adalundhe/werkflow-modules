from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetEventConfigurationRequest(BaseModel):
    TrailName: StrictStr | None = None
    EventDataStore: StrictStr | None = None
