from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TextractExpenseType(BaseModel):
    Text: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
