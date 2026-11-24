from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2LabelSummary(BaseModel):
    Name: StrictStr | None = None
