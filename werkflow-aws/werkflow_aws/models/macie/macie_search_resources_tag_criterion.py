from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .macie_search_resources_tag_criterion_pair import MacieSearchResourcesTagCriterionPair


class MacieSearchResourcesTagCriterion(BaseModel):
    comparator: Literal['EQ', 'NE'] | None = None
    tagValues: list[MacieSearchResourcesTagCriterionPair] | None = None
