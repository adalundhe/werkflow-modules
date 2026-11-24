from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexButton(BaseModel):
    text: StrictStr | None = None
    value: StrictStr | None = None
