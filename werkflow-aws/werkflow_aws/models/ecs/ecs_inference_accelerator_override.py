from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSInferenceAcceleratorOverride(BaseModel):
    deviceName: StrictStr | None = None
    deviceType: StrictStr | None = None
