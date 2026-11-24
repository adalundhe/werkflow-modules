from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SecurityHubNumberFilter(BaseModel):
    Gte: StrictFloat | StrictInt | None = None
    Lte: StrictFloat | StrictInt | None = None
    Eq: StrictFloat | StrictInt | None = None
    Gt: StrictFloat | StrictInt | None = None
    Lt: StrictFloat | StrictInt | None = None
