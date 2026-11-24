from __future__ import annotations
from pydantic import BaseModel, StrictInt


class JiraComponentField(BaseModel):
    componentId: StrictInt | None = None
