from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaEnvironment(BaseModel):
    Variables: dict[StrictStr, StrictStr] | None = None
