from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingOperator(BaseModel):
    Principal: StrictStr | None = None
