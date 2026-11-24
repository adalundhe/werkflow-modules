from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListStudiosRequest(BaseModel):
    Marker: StrictStr | None = None
