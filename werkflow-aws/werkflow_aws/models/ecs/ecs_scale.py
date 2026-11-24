from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ECSScale(BaseModel):
    value: StrictFloat | StrictInt | None = None
    unit: StrictStr | None = None
