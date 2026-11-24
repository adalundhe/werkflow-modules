from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class ConnectQuestionOptionPointsConfiguration(BaseModel):
    PointValue: StrictInt | None = None
    IsBonus: StrictBool | None = None
