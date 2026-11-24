from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractBoundingBoxConfiguration(BaseModel):
    State: StrictStr | None = None
