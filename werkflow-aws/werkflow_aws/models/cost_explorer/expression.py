from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_category import CostCategory
from .dimension import Dimension
from .tag_value import TagValue


class Expression(BaseModel):
    And: list[Expression] | None = None
    CostCategories: CostCategory | None = None
    Dimensions: Dimension | None = None
    Or: list[Expression] | None = None
    Not: Expression | None = None
    Tags: TagValue | None = None

    def dump(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
