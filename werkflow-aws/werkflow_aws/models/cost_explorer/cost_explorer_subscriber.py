from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSubscriber(BaseModel):
    Address: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
