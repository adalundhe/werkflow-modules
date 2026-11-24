from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeTunedHPOParams(BaseModel):
    algorithmHyperParameters: dict[StrictStr, StrictStr] | None = None
