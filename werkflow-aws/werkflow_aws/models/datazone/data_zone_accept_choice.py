from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneAcceptChoice(BaseModel):
    predictionTarget: StrictStr
    predictionChoice: StrictInt | None = None
    editedValue: StrictStr | None = None
