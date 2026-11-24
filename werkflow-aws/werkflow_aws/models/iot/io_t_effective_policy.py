from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTEffectivePolicy(BaseModel):
    policyName: StrictStr | None = None
    policyArn: StrictStr | None = None
    policyDocument: StrictStr | None = None
