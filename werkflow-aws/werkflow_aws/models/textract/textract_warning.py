from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TextractWarning(BaseModel):
    ErrorCode: StrictStr | None = None
    Pages: list[StrictInt] | None = None
