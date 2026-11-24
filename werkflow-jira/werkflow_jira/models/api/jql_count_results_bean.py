from __future__ import annotations
from pydantic import BaseModel, StrictInt


class JQLCountResultsBean(BaseModel):
    count: StrictInt | None = None
