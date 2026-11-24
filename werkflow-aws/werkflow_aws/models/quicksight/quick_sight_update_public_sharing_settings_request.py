from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightUpdatePublicSharingSettingsRequest(BaseModel):
    AwsAccountId: StrictStr
    PublicSharingEnabled: StrictBool | None = None
