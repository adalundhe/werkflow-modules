from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCatalystAccessTokenSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    expiresTime: datetime.datetime | StrictStr | None = None
