from __future__ import annotations
from pydantic import BaseModel
from .macie_search_resources_simple_criterion import MacieSearchResourcesSimpleCriterion
from .macie_search_resources_tag_criterion import MacieSearchResourcesTagCriterion


class MacieSearchResourcesCriteria(BaseModel):
    simpleCriterion: MacieSearchResourcesSimpleCriterion | None = None
    tagCriterion: MacieSearchResourcesTagCriterion | None = None
