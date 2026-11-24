from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractSplitterConfiguration(BaseModel):
    State: StrictStr | None = None
