from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LambdaContextOptions(BaseModel):
    ReplayChildren: StrictBool | None = None
