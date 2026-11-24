from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowPrefixConfig(BaseModel):
    prefixType: StrictStr | None = None
    prefixFormat: StrictStr | None = None
    pathPrefixHierarchy: list[StrictStr] | None = None
