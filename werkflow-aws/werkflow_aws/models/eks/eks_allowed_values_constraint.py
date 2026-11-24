from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAllowedValuesConstraint(BaseModel):
    allowedValues: list[StrictStr] | None = None
