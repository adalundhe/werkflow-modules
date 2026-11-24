from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeContentRedaction(BaseModel):
    RedactionType: StrictStr | None = None
    RedactionOutput: StrictStr | None = None
    PiiEntityTypes: list[StrictStr] | None = None
