from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAlarm(BaseModel):
    Name: StrictStr | None = None
