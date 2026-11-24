from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraDateInput(BaseModel):
    formattedDate: StrictStr | None = None
