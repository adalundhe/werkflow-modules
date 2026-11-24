from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowCustomerProfilesDestinationProperties(BaseModel):
    domainName: StrictStr | None = None
    objectTypeName: StrictStr | None = None
