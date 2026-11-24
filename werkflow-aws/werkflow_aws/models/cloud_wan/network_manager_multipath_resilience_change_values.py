from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerMultipathResilienceChangeValues(BaseModel):
    Mode: StrictStr | None = None
    EdgeSets: list[list[StrictStr]] | None = None
