from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRImageTagMutabilityExclusionFilter(BaseModel):
    filterType: StrictStr | None = None
    filter: StrictStr | None = None
