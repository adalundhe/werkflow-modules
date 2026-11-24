from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailMonitoredResourceInfo(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    resourceType: StrictStr | None = None
