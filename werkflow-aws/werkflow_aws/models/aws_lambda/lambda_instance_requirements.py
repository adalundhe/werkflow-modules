from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaInstanceRequirements(BaseModel):
    Architectures: list[StrictStr] | None = None
    AllowedInstanceTypes: list[StrictStr] | None = None
    ExcludedInstanceTypes: list[StrictStr] | None = None
