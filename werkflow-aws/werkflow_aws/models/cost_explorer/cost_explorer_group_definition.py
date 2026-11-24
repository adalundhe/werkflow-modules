from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerGroupDefinition(BaseModel):
    Type: StrictStr | None = None
    Key: StrictStr | None = None
