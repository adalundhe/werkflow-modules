from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2OnSourceDDoSProtectionConfig(BaseModel):
    ALBLowReputationMode: StrictStr | None = None
