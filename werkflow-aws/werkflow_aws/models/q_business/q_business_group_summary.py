from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGroupSummary(BaseModel):
    groupName: StrictStr | None = None
