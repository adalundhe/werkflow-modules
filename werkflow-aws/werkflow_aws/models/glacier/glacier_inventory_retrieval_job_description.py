from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierInventoryRetrievalJobDescription(BaseModel):
    Format: StrictStr | None = None
    StartDate: StrictStr | None = None
    EndDate: StrictStr | None = None
    Limit: StrictStr | None = None
    Marker: StrictStr | None = None
