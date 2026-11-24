from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneRejectChoice(BaseModel):
    predictionTarget: StrictStr
    predictionChoices: list[StrictInt] | None = None
