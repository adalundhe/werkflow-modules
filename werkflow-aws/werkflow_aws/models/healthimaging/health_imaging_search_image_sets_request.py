from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .health_imaging_search_criteria import HealthImagingSearchCriteria


class HealthImagingSearchImageSetsRequest(BaseModel):
    datastoreId: StrictStr
    searchCriteria: HealthImagingSearchCriteria | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
