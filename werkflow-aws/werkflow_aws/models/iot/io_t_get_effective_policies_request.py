from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetEffectivePoliciesRequest(BaseModel):
    principal: StrictStr | None = None
    cognitoIdentityPoolId: StrictStr | None = None
    thingName: StrictStr | None = None
