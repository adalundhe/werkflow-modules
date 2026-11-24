from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListPolicyPrincipalsRequest(BaseModel):
    policyName: StrictStr
    marker: StrictStr | None = None
    pageSize: StrictInt | None = None
    ascendingOrder: StrictBool | None = None
