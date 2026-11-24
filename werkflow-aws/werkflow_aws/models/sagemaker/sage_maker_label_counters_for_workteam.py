from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerLabelCountersForWorkteam(BaseModel):
    HumanLabeled: StrictInt | None = None
    PendingHuman: StrictInt | None = None
    Total: StrictInt | None = None
