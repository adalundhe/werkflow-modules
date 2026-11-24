from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FISActionParameter(BaseModel):
    description: StrictStr | None = None
    required: StrictBool | None = None
