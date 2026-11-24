from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateAccessTokenResponse(BaseModel):
    secret: StrictStr | None = None
    name: StrictStr | None = None
    expiresTime: datetime.datetime | StrictStr | None = None
    accessTokenId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
