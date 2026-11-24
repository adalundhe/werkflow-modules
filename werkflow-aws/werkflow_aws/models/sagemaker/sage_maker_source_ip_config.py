from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSourceIpConfig(BaseModel):
    Cidrs: list[StrictStr] | None = None
