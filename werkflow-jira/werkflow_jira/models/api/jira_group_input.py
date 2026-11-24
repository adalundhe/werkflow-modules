from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraGroupInput(BaseModel):
    groupName: StrictStr | None = None
