from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class QuickSightGetDashboardEmbedUrlRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    IdentityType: Literal['IAM', 'QUICKSIGHT', 'ANONYMOUS']
    SessionLifetimeInMinutes: StrictInt | None = None
    UndoRedoDisabled: StrictBool | None = None
    ResetDisabled: StrictBool | None = None
    StatePersistenceEnabled: StrictBool | None = None
    UserArn: StrictStr | None = None
    Namespace: StrictStr | None = None
    AdditionalDashboardIds: list[StrictStr] | None = None
