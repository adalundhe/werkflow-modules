from __future__ import annotations
from pydantic import BaseModel, StrictInt


class JiraSelectedOptionField(BaseModel):
    optionId: StrictInt | None = None
