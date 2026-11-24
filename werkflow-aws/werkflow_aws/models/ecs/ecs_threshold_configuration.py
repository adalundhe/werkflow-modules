from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSThresholdConfiguration(BaseModel):
    type: StrictStr | None = None
    value: StrictInt | None = None
