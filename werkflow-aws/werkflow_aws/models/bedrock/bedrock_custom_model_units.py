from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockCustomModelUnits(BaseModel):
    customModelUnitsPerModelCopy: StrictInt | None = None
    customModelUnitsVersion: StrictStr | None = None
