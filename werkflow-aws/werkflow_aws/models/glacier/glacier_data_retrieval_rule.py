from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlacierDataRetrievalRule(BaseModel):
    Strategy: StrictStr | None = None
    BytesPerHour: StrictInt | None = None
