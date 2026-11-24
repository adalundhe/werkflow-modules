from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftGetIdentityCenterAuthTokenResponse(BaseModel):
    Token: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
