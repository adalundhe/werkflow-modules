from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRSigningRepositoryFilter(BaseModel):
    filter: StrictStr | None = None
    filterType: StrictStr | None = None
