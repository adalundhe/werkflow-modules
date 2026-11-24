from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildProjectCache(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    modes: list[StrictStr] | None = None
    cacheNamespace: StrictStr | None = None
