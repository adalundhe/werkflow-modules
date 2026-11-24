from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .location_jobs_filter import LocationJobsFilter


class LocationListJobsRequest(BaseModel):
    Filter: LocationJobsFilter | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
