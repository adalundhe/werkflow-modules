from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingTrafficSourceIdentifier(BaseModel):
    Identifier: StrictStr | None = None
    Type: StrictStr | None = None
