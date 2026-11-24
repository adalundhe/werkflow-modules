from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_capabilities import QuickSightCapabilities
from .quick_sight_governance import QuickSightGovernance


class QuickSightCustomPermissions(BaseModel):
    Arn: StrictStr | None = None
    CustomPermissionsName: StrictStr | None = None
    Capabilities: QuickSightCapabilities | None = None
    Governance: QuickSightGovernance | None = None
