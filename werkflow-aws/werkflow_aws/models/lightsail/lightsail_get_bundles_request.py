from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetBundlesRequest(BaseModel):
    includeInactive: StrictBool | None = None
    pageToken: StrictStr | None = None
    appCategory: Literal['LfR'] | None = None
