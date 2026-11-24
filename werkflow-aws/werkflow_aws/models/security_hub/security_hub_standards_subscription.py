from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_standards_status_reason import SecurityHubStandardsStatusReason


class SecurityHubStandardsSubscription(BaseModel):
    StandardsSubscriptionArn: StrictStr | None = None
    StandardsArn: StrictStr | None = None
    StandardsInput: dict[StrictStr, StrictStr] | None = None
    StandardsStatus: StrictStr | None = None
    StandardsControlsUpdatable: StrictStr | None = None
    StandardsStatusReason: SecurityHubStandardsStatusReason | None = None
    Provider: StrictStr | None = None
