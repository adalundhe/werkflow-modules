from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDeleteFlywheelRequest(BaseModel):
    FlywheelArn: StrictStr
