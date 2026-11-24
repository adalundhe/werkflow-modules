from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailWafBotControlConfig(BaseModel):
    inspectionLevel: StrictStr | None = None
