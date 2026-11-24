from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_folder_search_filter import QuickSightFolderSearchFilter


class QuickSightSearchFoldersRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightFolderSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
