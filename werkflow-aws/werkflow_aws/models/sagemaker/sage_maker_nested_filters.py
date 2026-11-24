from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_filter import SageMakerFilter


class SageMakerNestedFilters(BaseModel):
    NestedPropertyName: StrictStr
    Filters: list[SageMakerFilter]
