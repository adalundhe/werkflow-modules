from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendRedactionConfig(BaseModel):
    PiiEntityTypes: list[StrictStr] | None = None
    MaskMode: StrictStr | None = None
    MaskCharacter: StrictStr | None = None
