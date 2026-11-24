from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2Limit(BaseModel):
    Name: StrictStr | None = None
    Max: StrictStr | None = None
