from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .macie_search_resources_criteria import MacieSearchResourcesCriteria


class MacieSearchResourcesCriteriaBlock(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    and_: list[MacieSearchResourcesCriteria] | None = Field(default=None, alias='and')
