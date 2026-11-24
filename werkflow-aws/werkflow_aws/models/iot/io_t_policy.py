from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPolicy(BaseModel):
    policyName: StrictStr | None = None
    policyArn: StrictStr | None = None
