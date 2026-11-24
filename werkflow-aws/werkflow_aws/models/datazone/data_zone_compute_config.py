from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneComputeConfig(BaseModel):
    instanceType: StrictStr | None = None
    environmentVersion: StrictStr | None = None
