from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailR53HostedZoneDeletionState(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
