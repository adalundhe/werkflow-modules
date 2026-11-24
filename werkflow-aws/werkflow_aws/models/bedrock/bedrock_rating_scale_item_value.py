from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockRatingScaleItemValue(BaseModel):
    stringValue: StrictStr | None = None
    floatValue: StrictFloat | StrictInt | None = None
