from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFilter(BaseModel):
    Pattern: StrictStr | None = None
