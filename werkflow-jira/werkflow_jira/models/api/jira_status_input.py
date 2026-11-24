from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraStatusInput(BaseModel):
    statusId: StrictStr | None = None
