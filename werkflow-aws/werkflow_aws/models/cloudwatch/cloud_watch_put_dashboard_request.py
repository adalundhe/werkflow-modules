from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutDashboardRequest(BaseModel):
    DashboardName: StrictStr
    DashboardBody: StrictStr
    Tags: list[CloudWatchTagModel] | None = None
