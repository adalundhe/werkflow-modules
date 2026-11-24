from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessAccessPolicyStats(BaseModel):
    DataPolicyCount: StrictInt | None = None
