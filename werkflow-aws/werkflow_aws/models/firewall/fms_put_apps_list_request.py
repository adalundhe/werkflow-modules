from __future__ import annotations
from pydantic import BaseModel
from .fms_apps_list_data import FMSAppsListData
from .fms_tag import FMSTag


class FMSPutAppsListRequest(BaseModel):
    AppsList: FMSAppsListData
    TagList: list[FMSTag] | None = None
