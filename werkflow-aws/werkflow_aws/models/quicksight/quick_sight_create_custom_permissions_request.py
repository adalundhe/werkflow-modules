from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_capabilities import QuickSightCapabilities
from .quick_sight_governance import QuickSightGovernance
from .quick_sight_tag import QuickSightTag


class QuickSightCreateCustomPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    CustomPermissionsName: StrictStr
    Capabilities: QuickSightCapabilities | None = None
    Governance: QuickSightGovernance | None = None
    Tags: list[QuickSightTag] | None = None
