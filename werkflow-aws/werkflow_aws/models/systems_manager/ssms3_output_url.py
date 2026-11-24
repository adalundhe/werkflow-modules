from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMS3OutputUrl(BaseModel):
    OutputUrl: StrictStr | None = None
