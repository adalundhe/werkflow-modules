from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexDTMFSpecification(BaseModel):
    maxLength: StrictInt | None = None
    endTimeoutMs: StrictInt | None = None
    deletionCharacter: StrictStr | None = None
    endCharacter: StrictStr | None = None
