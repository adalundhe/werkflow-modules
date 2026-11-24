from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractDeleteBlueprintRequest(BaseModel):
    BlueprintArn: StrictStr
    BlueprintVersion: StrictStr | None = None
