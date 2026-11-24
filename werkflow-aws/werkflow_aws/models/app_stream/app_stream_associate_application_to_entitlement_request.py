from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAssociateApplicationToEntitlementRequest(BaseModel):
    StackName: StrictStr
    EntitlementName: StrictStr
    ApplicationIdentifier: StrictStr
