from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightUpdateAccountSettingsRequest(BaseModel):
    AwsAccountId: StrictStr
    DefaultNamespace: StrictStr
    NotificationEmail: StrictStr | None = None
    TerminationProtectionEnabled: StrictBool | None = None
