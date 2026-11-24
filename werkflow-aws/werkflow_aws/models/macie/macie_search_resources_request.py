from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_search_resources_bucket_criteria import MacieSearchResourcesBucketCriteria
from .macie_search_resources_sort_criteria import MacieSearchResourcesSortCriteria


class MacieSearchResourcesRequest(BaseModel):
    bucketCriteria: MacieSearchResourcesBucketCriteria | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortCriteria: MacieSearchResourcesSortCriteria | None = None
