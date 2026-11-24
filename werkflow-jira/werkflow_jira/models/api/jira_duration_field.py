from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraDurationField(BaseModel):
    originalEstimateField: StrictStr | None = None
