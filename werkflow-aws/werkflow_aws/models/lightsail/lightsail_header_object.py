from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailHeaderObject(BaseModel):
    option: StrictStr | None = None
    headersAllowList: list[StrictStr] | None = None
