from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_apps_list_data import FMSAppsListData


class FMSPutAppsListResponse(BaseModel):
    AppsList: FMSAppsListData | None = None
    AppsListArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
