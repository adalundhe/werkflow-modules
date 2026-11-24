from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaAccountUsage(BaseModel):
    TotalCodeSize: StrictInt | None = None
    FunctionCount: StrictInt | None = None
