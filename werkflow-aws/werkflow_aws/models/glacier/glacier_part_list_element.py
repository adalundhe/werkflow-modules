from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierPartListElement(BaseModel):
    RangeInBytes: StrictStr | None = None
    SHA256TreeHash: StrictStr | None = None
