from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyLexicon(BaseModel):
    Content: StrictStr | None = None
    Name: StrictStr | None = None
