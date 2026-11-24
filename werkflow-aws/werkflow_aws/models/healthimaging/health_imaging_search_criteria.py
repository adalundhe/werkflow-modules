from __future__ import annotations
from pydantic import BaseModel
from .health_imaging_search_filter import HealthImagingSearchFilter
from .health_imaging_sort import HealthImagingSort


class HealthImagingSearchCriteria(BaseModel):
    filters: list[HealthImagingSearchFilter] | None = None
    sort: HealthImagingSort | None = None
