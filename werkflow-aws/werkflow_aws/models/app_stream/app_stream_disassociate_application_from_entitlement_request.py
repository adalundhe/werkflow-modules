from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDisassociateApplicationFromEntitlementRequest(BaseModel):
    StackName: StrictStr
    EntitlementName: StrictStr
    ApplicationIdentifier: StrictStr
