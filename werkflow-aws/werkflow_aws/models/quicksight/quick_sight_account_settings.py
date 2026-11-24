from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightAccountSettings(BaseModel):
    AccountName: StrictStr | None = None
    Edition: StrictStr | None = None
    DefaultNamespace: StrictStr | None = None
    NotificationEmail: StrictStr | None = None
    PublicSharingEnabled: StrictBool | None = None
    TerminationProtectionEnabled: StrictBool | None = None
