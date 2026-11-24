from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectValidationEnum(BaseModel):
    Strict: StrictBool | None = None
    Values: list[StrictStr] | None = None
