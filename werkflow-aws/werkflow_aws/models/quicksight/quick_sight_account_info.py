from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAccountInfo(BaseModel):
    AccountName: StrictStr | None = None
    Edition: StrictStr | None = None
    NotificationEmail: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    AccountSubscriptionStatus: StrictStr | None = None
    IAMIdentityCenterInstanceArn: StrictStr | None = None
