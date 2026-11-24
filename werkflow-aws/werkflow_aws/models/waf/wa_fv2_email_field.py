from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2EmailField(BaseModel):
    Identifier: StrictStr | None = None
