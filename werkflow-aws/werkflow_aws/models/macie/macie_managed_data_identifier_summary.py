from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieManagedDataIdentifierSummary(BaseModel):
    category: StrictStr | None = None
    id: StrictStr | None = None
