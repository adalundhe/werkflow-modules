from __future__ import annotations
from pydantic import BaseModel, StrictInt


class JiraExpressionsComplexityValueBean(BaseModel):
    limit: StrictInt | None = None
    value: StrictInt | None = None
