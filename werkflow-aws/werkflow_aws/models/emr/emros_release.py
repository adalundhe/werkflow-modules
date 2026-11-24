from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMROSRelease(BaseModel):
    Label: StrictStr | None = None
