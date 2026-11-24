from __future__ import annotations
from pydantic import BaseModel
from .macie_matching_bucket import MacieMatchingBucket


class MacieMatchingResource(BaseModel):
    matchingBucket: MacieMatchingBucket | None = None
