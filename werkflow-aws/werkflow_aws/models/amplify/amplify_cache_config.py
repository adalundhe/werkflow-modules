from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCacheConfig(BaseModel):
    type: StrictStr | None = None
