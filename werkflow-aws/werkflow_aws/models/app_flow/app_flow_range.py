from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class AppFlowRange(BaseModel):
    maximum: StrictFloat | StrictInt | None = None
    minimum: StrictFloat | StrictInt | None = None
