from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMListPoliciesGrantingServiceAccessRequest(BaseModel):
    Arn: StrictStr
    ServiceNamespaces: list[StrictStr]
    Marker: StrictStr | None = None
