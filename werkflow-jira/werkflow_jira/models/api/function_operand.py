from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FunctionOperand(BaseModel):
    arguments: list[StrictStr] | None = None
    encodedOperand: StrictStr | None = None
    function: StrictStr | None = None
