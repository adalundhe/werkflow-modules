from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRRepositoryFilter(BaseModel):
    filter: StrictStr | None = None
    filterType: StrictStr | None = None
