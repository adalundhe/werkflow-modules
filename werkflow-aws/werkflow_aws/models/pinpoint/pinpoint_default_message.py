from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDefaultMessage(BaseModel):
    Body: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
