from __future__ import annotations
from pydantic import BaseModel
from .macie_search_resources_criteria_block import MacieSearchResourcesCriteriaBlock


class MacieSearchResourcesBucketCriteria(BaseModel):
    excludes: MacieSearchResourcesCriteriaBlock | None = None
    includes: MacieSearchResourcesCriteriaBlock | None = None
