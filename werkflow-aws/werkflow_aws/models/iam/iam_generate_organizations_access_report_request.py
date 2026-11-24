from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGenerateOrganizationsAccessReportRequest(BaseModel):
    EntityPath: StrictStr
    OrganizationsPolicyId: StrictStr | None = None
