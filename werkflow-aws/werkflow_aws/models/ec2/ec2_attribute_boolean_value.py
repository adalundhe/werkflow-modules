from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2AttributeBooleanValue(BaseModel):
    Value: StrictBool | None = None
