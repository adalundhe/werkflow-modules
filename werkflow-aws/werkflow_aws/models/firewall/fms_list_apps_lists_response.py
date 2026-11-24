from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_apps_list_data_summary import FMSAppsListDataSummary


class FMSListAppsListsResponse(BaseModel):
    AppsLists: list[FMSAppsListDataSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
