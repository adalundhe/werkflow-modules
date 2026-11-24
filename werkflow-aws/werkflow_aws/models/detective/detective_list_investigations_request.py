from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .detective_filter_criteria import DetectiveFilterCriteria
from .detective_sort_criteria import DetectiveSortCriteria


class DetectiveListInvestigationsRequest(BaseModel):
    GraphArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    FilterCriteria: DetectiveFilterCriteria | None = None
    SortCriteria: DetectiveSortCriteria | None = None
