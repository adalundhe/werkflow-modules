from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSPolicySummary(BaseModel):
    PolicyArn: StrictStr | None = None
    PolicyId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    ResourceType: StrictStr | None = None
    SecurityServiceType: StrictStr | None = None
    RemediationEnabled: StrictBool | None = None
    DeleteUnusedFMManagedResources: StrictBool | None = None
    PolicyStatus: StrictStr | None = None
