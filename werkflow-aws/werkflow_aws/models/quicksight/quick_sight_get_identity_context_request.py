from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_user_identifier import QuickSightUserIdentifier


class QuickSightGetIdentityContextRequest(BaseModel):
    AwsAccountId: StrictStr
    UserIdentifier: QuickSightUserIdentifier
    Namespace: StrictStr | None = None
    SessionExpiresAt: datetime.datetime | StrictStr | None = None
    ContextRegion: StrictStr | None = None
