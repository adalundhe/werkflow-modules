from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailInstanceHealthSummary(BaseModel):
    instanceName: StrictStr | None = None
    instanceHealth: StrictStr | None = None
    instanceHealthReason: StrictStr | None = None
