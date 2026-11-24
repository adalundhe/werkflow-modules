from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAlarmStateInformation(BaseModel):
    Name: StrictStr | None = None
    State: StrictStr | None = None
