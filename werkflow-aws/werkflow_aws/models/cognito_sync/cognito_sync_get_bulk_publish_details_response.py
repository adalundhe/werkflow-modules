from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoSyncGetBulkPublishDetailsResponse(BaseModel):
    IdentityPoolId: StrictStr | None = None
    BulkPublishStartTime: datetime.datetime | StrictStr | None = None
    BulkPublishCompleteTime: datetime.datetime | StrictStr | None = None
    BulkPublishStatus: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
