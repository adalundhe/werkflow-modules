from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSInferenceAccelerator(BaseModel):
    deviceName: StrictStr | None = None
    deviceType: StrictStr | None = None
