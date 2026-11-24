from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSecurityProfileTarget(BaseModel):
    arn: StrictStr | None = None
