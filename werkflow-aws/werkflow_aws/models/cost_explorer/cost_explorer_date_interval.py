from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerDateInterval(BaseModel):
    Start: StrictStr | None = None
    End: StrictStr | None = None
