from __future__ import annotations
from pydantic import BaseModel
from .connect_categories_attribute_and_condition import ConnectCategoriesAttributeAndCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectCategoriesAttributeFilter(BaseModel):
    OrConditions: list[ConnectCategoriesAttributeAndCondition] | None = None
    AndCondition: ConnectCategoriesAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
