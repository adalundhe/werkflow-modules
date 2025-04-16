from __future__ import annotations
from pydantic import BaseModel
from .cost_category import CostCategory
from .dimension import Dimension
from .tag_value import TagValue

class Expression(BaseModel):
    And: list[Expression] | None = None
    CostCategories: list[CostCategory] | None = None
    Dimensions: Dimension | None = None
    Or: list[Expression] | None = None
    Not: list[Expression] | None = None
    Tags: list[TagValue] | None = None

    def dump(self):
        return self.model_dump(exclude_none=True)