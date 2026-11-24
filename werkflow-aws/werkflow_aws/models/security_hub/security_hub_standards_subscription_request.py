from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsSubscriptionRequest(BaseModel):
    StandardsArn: StrictStr
    StandardsInput: dict[StrictStr, StrictStr] | None = None
