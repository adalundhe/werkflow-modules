from __future__ import annotations
from pydantic import BaseModel, StrictBool


class HealthImagingOverrides(BaseModel):
    forced: StrictBool | None = None
