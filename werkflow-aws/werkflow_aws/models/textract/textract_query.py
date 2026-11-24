from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractQuery(BaseModel):
    Text: StrictStr | None = None
    Alias: StrictStr | None = None
    Pages: list[StrictStr] | None = None
