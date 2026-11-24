from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateAccessTokenRequest(BaseModel):
    name: StrictStr
    expiresTime: datetime.datetime | StrictStr | None = None
