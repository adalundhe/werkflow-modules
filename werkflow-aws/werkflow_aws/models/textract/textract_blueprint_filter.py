from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractBlueprintFilter(BaseModel):
    BlueprintArn: StrictStr
    BlueprintVersion: StrictStr | None = None
