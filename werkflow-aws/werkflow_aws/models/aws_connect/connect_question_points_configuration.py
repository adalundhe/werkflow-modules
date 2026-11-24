from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class ConnectQuestionPointsConfiguration(BaseModel):
    MaxPointValue: StrictInt | None = None
    MinPointValue: StrictInt | None = None
    IsBonus: StrictBool | None = None
