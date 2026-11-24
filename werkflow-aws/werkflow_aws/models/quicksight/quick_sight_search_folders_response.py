from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_folder_summary import QuickSightFolderSummary


class QuickSightSearchFoldersResponse(BaseModel):
    Status: StrictInt | None = None
    FolderSummaryList: list[QuickSightFolderSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
