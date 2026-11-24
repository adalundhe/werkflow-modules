from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cognito_idp_restore_preview_type import CognitoIDPRestorePreviewType


class CognitoIDPRestorationType(BaseModel):
    RestoreId: StrictStr | None = None
    RestoreStatus: StrictStr | None = None
    RestoreTimestamp: datetime.datetime | StrictStr | None = None
    TriggerTimestamp: datetime.datetime | StrictStr | None = None
    RestorePreview: list[CognitoIDPRestorePreviewType] | None = None
