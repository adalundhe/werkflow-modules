from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSLogDriverVolumeConfiguration(BaseModel):
    driver: StrictStr | None = None
