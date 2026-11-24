from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BulkProjectPolicyRequest(BaseModel):
    projectIds: list[StrictInt] | None = None
