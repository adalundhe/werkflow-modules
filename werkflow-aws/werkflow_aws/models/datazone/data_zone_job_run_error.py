from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneJobRunError(BaseModel):
    message: StrictStr | None = None
