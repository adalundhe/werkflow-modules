from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierInventoryRetrievalJobInput(BaseModel):
    StartDate: StrictStr | None = None
    EndDate: StrictStr | None = None
    Limit: StrictStr | None = None
    Marker: StrictStr | None = None
