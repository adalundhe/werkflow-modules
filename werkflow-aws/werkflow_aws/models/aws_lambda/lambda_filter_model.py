from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFilterModel(BaseModel):
    Pattern: StrictStr | None = None
