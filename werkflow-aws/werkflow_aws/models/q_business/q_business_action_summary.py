from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessActionSummary(BaseModel):
    actionIdentifier: StrictStr | None = None
    displayName: StrictStr | None = None
    instructionExample: StrictStr | None = None
    description: StrictStr | None = None
