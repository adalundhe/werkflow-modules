from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSFailedItem(BaseModel):
    URI: StrictStr | None = None
    Reason: StrictStr | None = None
