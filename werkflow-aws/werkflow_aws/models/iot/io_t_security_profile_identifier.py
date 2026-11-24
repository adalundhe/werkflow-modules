from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSecurityProfileIdentifier(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
