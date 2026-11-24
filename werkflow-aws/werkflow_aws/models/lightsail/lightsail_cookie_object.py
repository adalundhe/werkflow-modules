from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCookieObject(BaseModel):
    option: StrictStr | None = None
    cookiesAllowList: list[StrictStr] | None = None
