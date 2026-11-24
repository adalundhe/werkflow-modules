from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractExpenseGroupProperty(BaseModel):
    Types: list[StrictStr] | None = None
    Id: StrictStr | None = None
