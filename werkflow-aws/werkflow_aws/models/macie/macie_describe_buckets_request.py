from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_bucket_criteria_additional_properties import MacieBucketCriteriaAdditionalProperties
from .macie_bucket_sort_criteria import MacieBucketSortCriteria


class MacieDescribeBucketsRequest(BaseModel):
    criteria: dict[StrictStr, MacieBucketCriteriaAdditionalProperties] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortCriteria: MacieBucketSortCriteria | None = None
