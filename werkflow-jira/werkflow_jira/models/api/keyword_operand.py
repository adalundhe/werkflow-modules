from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KeywordOperand(BaseModel):
    keyword: StrictStr | None = None
