from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_list_jobs_filter_criteria import MacieListJobsFilterCriteria
from .macie_list_jobs_sort_criteria import MacieListJobsSortCriteria


class MacieListClassificationJobsRequest(BaseModel):
    filterCriteria: MacieListJobsFilterCriteria | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortCriteria: MacieListJobsSortCriteria | None = None
