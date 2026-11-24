from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMTarget(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
