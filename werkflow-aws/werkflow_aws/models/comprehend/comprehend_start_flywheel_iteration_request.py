from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStartFlywheelIterationRequest(BaseModel):
    FlywheelArn: StrictStr
    ClientRequestToken: StrictStr | None = None
