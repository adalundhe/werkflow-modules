from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2LabelNameCondition(BaseModel):
    LabelName: StrictStr | None = None
