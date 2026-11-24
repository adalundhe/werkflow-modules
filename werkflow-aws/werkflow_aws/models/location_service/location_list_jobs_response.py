from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_jobs_response_entry import LocationListJobsResponseEntry


class LocationListJobsResponse(BaseModel):
    Entries: list[LocationListJobsResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
