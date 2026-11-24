from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .health_imaging_search_by_attribute_value import HealthImagingSearchByAttributeValue


class HealthImagingSearchFilter(BaseModel):
    values: list[HealthImagingSearchByAttributeValue]
    operator: Literal['EQUAL', 'BETWEEN']
