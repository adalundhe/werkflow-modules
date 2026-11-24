from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractBlueprintItem(BaseModel):
    BlueprintArn: StrictStr | None = None
    BlueprintVersion: StrictStr | None = None
