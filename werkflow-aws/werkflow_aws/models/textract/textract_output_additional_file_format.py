from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractOutputAdditionalFileFormat(BaseModel):
    State: StrictStr | None = None
