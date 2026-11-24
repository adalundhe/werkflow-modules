from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerEffectivePreferredResource(BaseModel):
    name: StrictStr | None = None
    includeList: list[StrictStr] | None = None
    effectiveIncludeList: list[StrictStr] | None = None
    excludeList: list[StrictStr] | None = None
