from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StepFunctionsMapStateStartedEventDetails(BaseModel):
    length: StrictInt | None = None
