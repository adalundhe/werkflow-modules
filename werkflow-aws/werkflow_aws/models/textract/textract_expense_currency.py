from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TextractExpenseCurrency(BaseModel):
    Code: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
