from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraDateTimeInput(BaseModel):
    formattedDateTime: StrictStr | None = None
