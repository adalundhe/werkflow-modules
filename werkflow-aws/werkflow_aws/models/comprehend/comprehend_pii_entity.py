from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendPiiEntity(BaseModel):
    Score: StrictFloat | StrictInt | None = None
    Type: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
