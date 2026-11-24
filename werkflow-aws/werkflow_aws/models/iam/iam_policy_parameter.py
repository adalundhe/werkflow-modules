from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPolicyParameter(BaseModel):
    Name: StrictStr | None = None
    Values: list[StrictStr] | None = None
    Type: StrictStr | None = None
