from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FISTargetResourceTypeParameter(BaseModel):
    description: StrictStr | None = None
    required: StrictBool | None = None
