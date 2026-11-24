from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyListLexiconsRequest(BaseModel):
    NextToken: StrictStr | None = None
