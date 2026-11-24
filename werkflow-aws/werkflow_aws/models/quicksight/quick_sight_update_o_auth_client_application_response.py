from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateOAuthClientApplicationResponse(BaseModel):
    Arn: StrictStr | None = None
    OAuthClientApplicationId: StrictStr | None = None
    UpdateStatus: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
