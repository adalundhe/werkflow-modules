from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractPIIEntitiesConfiguration(BaseModel):
    PiiEntityTypes: list[StrictStr] | None = None
    RedactionMaskMode: StrictStr | None = None
