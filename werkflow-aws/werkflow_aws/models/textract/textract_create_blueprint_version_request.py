from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractCreateBlueprintVersionRequest(BaseModel):
    BlueprintArn: StrictStr
    ClientRequestToken: StrictStr | None = None
